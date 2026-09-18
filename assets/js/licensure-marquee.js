/* Licensure marquee on the homepage.
 *
 * Progressive enhancement. Without this script the licence row is an ordinary
 * wrapping row showing all six states, which is what the page had before the
 * marquee existed. This script turns it into a single line that scrolls
 * continuously and can be dragged with a mouse or a finger.
 *
 * The scrolling is driven by the container's own scrollLeft rather than by a
 * transform, so a finger drag is handled natively, with the platform's own
 * momentum, and a mouse drag only needs the pointer handlers below.
 */
(function () {
  "use strict";

  var marquee = document.querySelector(".license-marquee");
  if (!marquee) return;

  var track = marquee.querySelector(".license-track");
  if (!track) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  var LOOP_SECONDS = 36;   // Matches the speed the owner approved.
  var RESUME_AFTER = 2500; // Idle time before the drift starts again.

  var pos = 0;             // Kept as a float, since scrollLeft may be rounded.
  var unit = 0;            // Width of the repeating unit, in pixels.
  var running = false;
  var interacting = false;
  var lastTime = 0;
  var frame = 0;
  var idleTimer = 0;
  var resizeTimer = 0;

  var group = track.querySelector(".license-group");
  if (!group) return;

  /* A loop is only seamless when the repeating unit is at least as wide as the
     visible container, otherwise the jump back exposes content the viewer can
     see. One group is narrower than the container at most widths, so clone the
     group until a unit is wide enough, then lay down two units. */
  function build() {
    var clones = track.querySelectorAll(".license-group[data-clone]");
    for (var i = 0; i < clones.length; i++) clones[i].remove();

    var groupWidth = group.getBoundingClientRect().width;
    if (!groupWidth) return 0;

    var perUnit = Math.max(1, Math.ceil(marquee.clientWidth / groupWidth));
    for (var j = 1; j < perUnit * 2; j++) {
      var copy = group.cloneNode(true);
      copy.setAttribute("aria-hidden", "true");
      copy.setAttribute("data-clone", "");
      track.appendChild(copy);
    }
    return perUnit * groupWidth;
  }

  function wrap() {
    if (unit <= 0) return;
    if (marquee.scrollLeft >= unit) {
      marquee.scrollLeft -= unit;
    } else if (interacting && marquee.scrollLeft <= 0) {
      marquee.scrollLeft += unit;
    }
  }

  function step(now) {
    if (!running) return;
    if (!lastTime) lastTime = now;
    var dt = (now - lastTime) / 1000;
    lastTime = now;

    if (unit > 0) {
      pos += (unit / LOOP_SECONDS) * dt;
      if (pos >= unit) pos -= unit;
      marquee.scrollLeft = pos;
    }
    frame = window.requestAnimationFrame(step);
  }

  function start() {
    if (running || reduce.matches || interacting || unit <= 0) return;
    pos = marquee.scrollLeft;                  // Resync after any interaction.
    running = true;
    lastTime = 0;
    frame = window.requestAnimationFrame(step);
  }

  function stop() {
    running = false;
    window.cancelAnimationFrame(frame);
  }

  function holdThenResume() {
    stop();
    window.clearTimeout(idleTimer);
    idleTimer = window.setTimeout(start, RESUME_AFTER);
  }

  function layout() {
    stop();
    marquee.scrollLeft = 0;
    pos = 0;
    unit = build();
    start();
  }

  /* Mouse drag. Touch is left to the browser, which scrolls the container
     natively and gives the momentum people expect. */
  var dragging = false;
  var startX = 0;
  var startScroll = 0;

  marquee.addEventListener("pointerdown", function (e) {
    if (e.pointerType !== "mouse" || e.button !== 0) return;
    dragging = true;
    interacting = true;
    startX = e.clientX;
    startScroll = marquee.scrollLeft;
    marquee.classList.add("is-dragging");
    stop();
    window.clearTimeout(idleTimer);
  });

  marquee.addEventListener("pointermove", function (e) {
    if (!dragging) return;
    e.preventDefault();

    var wanted = startScroll - (e.clientX - startX);
    marquee.scrollLeft = wanted;

    /* Crossing the seam moves the container by one group. Shift the reference
       by the same amount, so the content stays under the cursor. */
    if (unit > 0) {
      if (marquee.scrollLeft >= unit) {
        marquee.scrollLeft -= unit;
        startScroll -= unit;
      } else if (wanted <= 0) {
        marquee.scrollLeft += unit;
        startScroll += unit;
      }
    }
  });

  function endDrag() {
    if (!dragging) return;
    dragging = false;
    interacting = false;
    marquee.classList.remove("is-dragging");
    holdThenResume();
  }

  marquee.addEventListener("pointerup", endDrag);
  marquee.addEventListener("pointercancel", endDrag);
  marquee.addEventListener("pointerleave", endDrag);

  /* Finger and trackpad. */
  marquee.addEventListener("touchstart", function () {
    interacting = true;
    stop();
    window.clearTimeout(idleTimer);
  }, { passive: true });

  marquee.addEventListener("touchend", function () {
    interacting = false;
    holdThenResume();
  }, { passive: true });

  marquee.addEventListener("wheel", function () {
    holdThenResume();
  }, { passive: true });

  marquee.addEventListener("scroll", function () {
    if (!running) wrap();
  }, { passive: true });

  /* Pausing on hover and on keyboard focus was already the behaviour. */
  marquee.addEventListener("mouseenter", stop);
  marquee.addEventListener("mouseleave", function () {
    if (!dragging) holdThenResume();
  });
  marquee.addEventListener("focusin", stop);
  marquee.addEventListener("focusout", holdThenResume);

  /* Stop entirely while the tab is hidden, so a background tab is not
     animating for no reason. */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop();
    else start();
  });

  reduce.addEventListener("change", function () {
    if (reduce.matches) stop();
    else start();
  });

  window.addEventListener("resize", function () {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(layout, 200);
  });

  marquee.classList.add("is-marquee");

  /* Measure after the web fonts land, otherwise the group is measured in the
     fallback face and every width is wrong. */
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(layout);
  } else {
    layout();
  }
})();

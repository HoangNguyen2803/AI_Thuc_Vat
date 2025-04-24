// static/UI.js
// --------------------------------------------------
// 1. Hover sound (ngắn) + khởi động nhạc nền duy nhất
// --------------------------------------------------
const hoverSfx = '/static/hover.mp3';
const bgMusic  = '/static/music/study-music-for-focus-and-brain-power-432-hz-172844.mp3';

let bgStarted = false;
let bgAudio;

function playHover() {
  new Audio(hoverSfx).play();
}

function startBG() {
  if (bgStarted) return;
  bgStarted = true;
  bgAudio = new Audio(bgMusic);
  bgAudio.loop   = true;
  bgAudio.volume = 0.25;          // 25 % âm lượng – bạn chỉnh tùy ý
  bgAudio.play().catch(() => {
    // Nếu trình duyệt vẫn chặn (edge‑case), chờ click kế tiếp.
    bgStarted = false;
  });
}

// gán cho tất cả sector
document.querySelectorAll('.sector').forEach(sec => {
  sec.addEventListener('mouseenter', () => {
    playHover();
    startBG();
  });
  // cũng bật khi user click
  sec.addEventListener('click', startBG);
});

// --------------------------------------------------
// 2. Tô cánh sen theo % tiến độ
// --------------------------------------------------
fetch('/mandala/progress')
  .then(r => r.json())
  .then(data => {
    const pct    = data.percent || 0;
    const petals = document.querySelectorAll('.petal');
    const n      = Math.round(pct / (100 / petals.length));
    petals.forEach((p, i) => { if (i < n) p.classList.add('open'); });
  });

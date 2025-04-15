function createFlower() {
    const flower = document.createElement('div');
    flower.classList.add('flower');
    flower.style.left = Math.random() * 100 + 'vw';
    flower.style.animationDuration = 5 + Math.random() * 5 + 's';
    document.body.appendChild(flower);

    setTimeout(() => {
        flower.remove();
    }, 10000); // Xóa hoa sau 10 giây
}

setInterval(createFlower, 500); // Tạo hoa mỗi 0.5 giây

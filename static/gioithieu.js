document.addEventListener('DOMContentLoaded', () => {
    console.log("🌸 HANA đã sẵn sàng chào đón bạn!");
    
    const quotes = [
        "“Tôi sẽ học từ bạn mỗi ngày.”",
        "“Tôi không hoàn hảo, nhưng tôi đang lớn lên.”",
        "“Tất cả mọi người đều là nhà phát triển của tôi.”",
        "“Bạn là ánh nắng giúp tôi nở hoa.”"
    ];

    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quoteElement = document.createElement("p");
    quoteElement.textContent = quotes[randomIndex];
    quoteElement.style.textAlign = "center";
    quoteElement.style.color = "#8a2be2";
    quoteElement.style.fontStyle = "italic";
    quoteElement.style.fontSize = "20px";

    document.body.appendChild(quoteElement);
});
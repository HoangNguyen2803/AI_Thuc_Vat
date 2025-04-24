function submitGopy() {
    const gopy = document.getElementById("gopyInput").value.trim();
    if (!gopy) {
        alert("❗ Vui lòng nhập nội dung góp ý.");
        return;
    }

    const xacnhan = confirm(`Bạn muốn góp ý với nội dung:\n\n"${gopy}"\n\nđúng không?`);
    if (xacnhan) {
        fetch("/gopy", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ gopy: gopy })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("message").innerText = "✅ Cảm ơn bạn đã góp ý, chúng tôi đã ghi nhận!";
            document.getElementById("gopyInput").value = "";
        })
        .catch(err => {
            document.getElementById("message").innerText = "❌ Lỗi gửi góp ý.";
        });
    } else {
        document.getElementById("message").innerText = "⛔ Đã huỷ góp ý.";
    }
}

function goHome() {
    window.location.href = "/";
}
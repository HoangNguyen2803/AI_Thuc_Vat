<?php
$input = "nâng cấp hệ thống";

// Đường dẫn đến file app.py nằm ở thư mục cha của PHP_SQL
$pythonFile = realpath(__DIR__ . '\AI\app.py');

// escape dữ liệu đầu vào
$escaped_input = escapeshellarg($input);

// thực thi Python script
$command = "python3 $pythonFile $escaped_input";
$output = shell_exec($command);

echo "Kết quả AI xử lý: " . htmlspecialchars($output);
?>
// sửa lỗi 
<?php
echo "<pre>";
echo shell_exec("which python3"); // Kiểm tra đường dẫn python
echo shell_exec("python3 --version"); // Kiểm tra version
echo "</pre>";
?>

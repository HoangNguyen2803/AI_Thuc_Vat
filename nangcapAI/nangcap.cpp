#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <windows.h>

using namespace std;

// Căn trái thủ công cho wstring
wstring pad_left(const wstring& str, size_t width) {
    if (str.length() >= width) return str.substr(0, width);
    return str + wstring(width - str.length(), L' ');
}

// Hàm chuyển std::string (UTF-8) sang std::wstring
wstring string_to_wstring(const string& str) {
    int size_needed = MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, nullptr, 0);
    if (size_needed <= 0) return L"";
    wstring wstr(size_needed, 0);
    MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, &wstr[0], size_needed);
    wstr.pop_back(); // Xoá ký tự null ở cuối
    return wstr;
}

int main() {
    SetConsoleOutputCP(CP_UTF8);

    ifstream file("database.txt");
    if (!file) {
        wcout << L"❌ Không thể mở file 'database.txt'" << endl;
        return 1;
    }

    // Không thiết lập locale nữa để tránh lỗi
    // wcout.imbue(locale(""));  // Xóa dòng này
    //wcout.imbue(std::locale(""));  // thử thiết lập mặc định, nhưng nếu không ổn, chỉ cần bỏ dòng này

    string line;
    bool hasData = false;

    wcout << L"🌸 Danh sách hoa đã dạy cho AI:\n";
    wcout << L"---------------------------------------------------------------------\n";
    wcout << L"| " << pad_left(L"Tên (EN)", 15)
          << L" | " << pad_left(L"Tên tiếng Việt", 20)
          << L" | " << pad_left(L"Thông số (4)", 15) << L" |" << endl;
    wcout << L"---------------------------------------------------------------------\n";

    while (getline(file, line)) {
        if (line.empty()) continue;

        stringstream ss(line);
        string tenHoa, tenTViet, sl, sw, pl, pw;

        if (getline(ss, tenHoa, ',') &&
            getline(ss, tenTViet, ',') &&
            getline(ss, sl, ',') &&
            getline(ss, sw, ',') &&
            getline(ss, pl, ',') &&
            getline(ss, pw)) {

            string thongso = sl + ", " + sw + ", " + pl + ", " + pw;

            wstring wTenHoa = string_to_wstring(tenHoa);
            wstring wTenTViet = string_to_wstring(tenTViet);
            wstring wThongSo = string_to_wstring(thongso);

            wcout << L"| " << pad_left(wTenHoa, 15)
                  << L" | " << pad_left(wTenTViet, 20)
                  << L" | " << pad_left(wThongSo, 15) << L" |" << endl;

            hasData = true;
        }
    }

    if (!hasData) {
        wcout << L"|     (Không có dữ liệu hoa nào để hiển thị)                         |\n";
    }

    wcout << L"---------------------------------------------------------------------\n";
    file.close();

    return 0;
}

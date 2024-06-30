# randmatrix
GPTに感謝を  
↓ヴィジュアライザ  
https://gen3987.github.io/visualizer/    

testcasemaker.pyを作ったので、テストケースの生成はそちらを使ったほうが便利かも    

以下のコード(by GPT-4o)を書き換えることで、JSON形式のファイルに変換できる。  
```C++
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// 二次元配列を文字列ベースのベクターに変換する関数
std::vector<std::string> arrayToStringVector(const std::vector<std::vector<int>>& array) {
    std::vector<std::string> result;
    for (const auto& row : array) {
        std::string rowString;
        for (int value : row) {
            rowString += std::to_string(value);
        }
        result.push_back(rowString);
    }
    return result;
}

// 配列の状態をJSONに変換する関数
json arrayToJson(const std::vector<std::vector<int>>& array, int step) {
    json j;
    j[std::to_string(step)] = arrayToStringVector(array);
    return j;
}

int main() {
    // 初期の二次元配列
    std::vector<std::vector<int>> array = {
        {2, 0, 3, 1, 4},
        {4, 2, 3, 0, 1},
        {0, 1, 4, 3, 2},
        {1, 3, 4, 2, 0},
        {3, 4, 2, 1, 0}
    };

    // ボード情報を含むJSONオブジェクト
    json boardJson;
    boardJson["width"] = array[0].size();
    boardJson["height"] = array.size();

    // 配列の初期状態を記録
    int step = 0;
    boardJson.update(arrayToJson(array, step));

    // 複数回の変更を行う（ここでは例として3回の変更を行う）
    for (int i = 1; i <= 9; ++i) {
        // 配列の一部を変更
        array[i % array.size()][(i * 2) % array[0].size()] = (array[i % array.size()][(i * 2) % array[0].size()] + 1) % 4;
        
        // 変更後の配列を記録
        step++;
        boardJson.update(arrayToJson(array, step));
    }

    // JSONファイルに出力
    std::ofstream outFile("array_changes.json");
    json finalJson;
    finalJson["board"] = boardJson;
    outFile << finalJson.dump(4); // 4はインデントのスペース数
    outFile.close();

    std::cout << "Array changes have been written to array_changes.json." << std::endl;

    return 0;
}
```

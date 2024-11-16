# Setup

## JetBrains Fleet

Most solutions can be run in the [Fleet](https://www.jetbrains.com/fleet/) code editor by JetBrains
or [VS Code](https://code.visualstudio.com/). Below are the settings for the `run.json` file, which should be placed in
the `.fleet` directory located at the root of the project.

```json
{
  "configurations": [
    {
      "type": "command",
      "name": "Build C++",
      "program": "g++",
      "args": [
        "$FILE$",
        "-std=c++23",
        "-o",
        "bin/cpp/main"
      ]
    },
    {
      "type": "command",
      "name": "Run C++",
      "dependsOn": [
        "Build C++"
      ],
      "program": "$PROJECT_DIR$/bin/cpp/main.exe"
    },
    {
      "type": "command",
      "name": "Build C#",
      "program": "dotnet",
      "args": [
        "C:/Program Files/dotnet/sdk/8.0.300/Roslyn/bincore/csc.dll",
        "-target:exe",
        "-out:bin/csharp/Program.dll",
        "-lib:\"C:/Program Files/dotnet/shared/Microsoft.NETCore.App/8.0.5\"",
        "-reference:System.Private.CoreLib.dll",
        "-reference:System.Runtime.dll",
        "-reference:System.Console.dll",
        "-reference:System.Text.RegularExpressions.dll",
        "-main:Solution",
        "$FILE$"
      ]
    },
    {
      "type": "command",
      "name": "Run C#",
      "dependsOn": [
        "Build C#"
      ],
      "program": "dotnet",
      "args": [
        "$PROJECT_DIR$/bin/csharp/Program.dll"
      ]
    }
  ]
}
```

> For C# solutions, you may need to add additional references for your programs.

Before running, manually create a `bin` directory at the project root and add `cpp` and `csharp` subdirectories to
it.<br>
Add the following file `Program.runtimeconfig.json` to the `bin/csharp` directory:

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

> Make sure to check the versions you are using.

## C++

To run C++ code, install [MSYS2](https://www.msys2.org/) or use [Dev-C++](https://www.bloodshed.net/).

### Reading an unknown number of inputs

```c++
const int MAX_SIZE = 1000;

int array[MAX_SIZE];
int index = 0;
int input;

while (cin >> input) {
  array[index] = input;
  index++;
}
```

## C#

To run C# code, make sure to install the [.NET SDK](https://dotnet.microsoft.com/en-us/download).

## Python

For Python, you can use the default [Python IDLE](https://www.python.org/downloads/)
or [PyCharm](https://www.jetbrains.com/pycharm/).

## JavaScript

To run JS code, make sure [Node.js](https://nodejs.org/) is installed.

### I. Reading data

```javascript
var scanf = require('scanf');
var n = scanf('%d');

// ...
```

### II. Reading an unknown number of inputs

```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lines = [];

rl
  .on("line", line => lines.push(line))
  .on("close", () => {
    let [n, weights] = lines;

    n = +n;
    weights = weights?.split(' ').map(weight => +weight).slice(0, n) ?? [];

    solve(n, weights);
  });

function solve(n, weights) {
  // ...
}
```

## Pascal

To run Pascal code, you can use [Pascal XE](https://sourceforge.net/projects/pascalxe/) or PascalABC.NET.

## References

- [Installing MSYS2](https://code.visualstudio.com/docs/cpp/config-mingw#_installing-the-mingww64-toolchain)
- [Fleet. Getting started with C++](https://www.jetbrains.com/help/fleet/getting-started-with-cpp-in-fleet.html#cpp-buildrun-example)
- [Compile and Run C# programs without visual studio or any other IDE](https://dev.to/entangledcognition/execute-c-programs-without-visual-studio-or-any-other-ide-4g6n)
- [Fleet. Run configuration macros](https://www.jetbrains.com/help/fleet/built-in-macros.html)

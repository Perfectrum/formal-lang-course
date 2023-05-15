import subprocess
import shared


def main():
    shared.configure_python_path()
    subprocess.check_call(
        "antlr4 project/lang/lang.g4 -Dlanguage=Python3 -o project/lang/antlrgen -Xexact-output-dir -visitor".split(
            " "
        )
    )


if __name__ == "__main__":
    main()

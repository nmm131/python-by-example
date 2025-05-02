$files = @(
    "01_hello_world.py",
    "02_variables.py",
    "03_constants.py",
    "04_if_else.py",
    "05_loops.py",
    "06_functions.py",
    "07_lists.py",
    "08_dicts.py",
    "09_sets.py",
    "10_tuples.py",
    "11_comprehensions.py",
    "12_exceptions.py",
    "13_classes.py",
    "14_inheritance.py",
    "15_file_io.py",
    "16_json_handling.py",
    "17_pathlib_os.py",
    "18_argparse.py",
    "19_logging.py",
    "20_concurrency_intro.py"
)

foreach ($file in $files) {
    $content = @"
# $($file -replace '.py$', '') - Python by Example

def main():
    print("TODO: implement $file")

if __name__ == "__main__":
    main()
"@
    Set-Content -Path $file -Value $content -Force
}

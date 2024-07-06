from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but some might need fine tuning
build_exe_options = {
    "packages": ["os", "sys", "polars", "datashader", "plotly.io", "numpy"], 
    "excludes": ["tkinter"], 
    "include_files": ["utf_인천광역시_온도_202107.csv"],
    "includes": ["temperature_test_0704"]
}


setup(
    name="MyApp_0706",
    version="0.1",
    description="My PySide application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("pyside_0704.py", base="Win32GUI")]
)

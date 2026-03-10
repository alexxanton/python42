import importlib


def main() -> None:
    """
    Checks if the required modules are installed and performs
    a data analysis with matplotlib and pandas
    """
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    mods = {}
    required = ["pandas", "matplotlib", "requests"]
    module_not_found = False
    for x in required:
        try:
            mod = importlib.import_module(x)
            mods[mod.__name__] = mod
            print(f"[OK] {mod.__name__} ({mod.__version__})")
        except ModuleNotFoundError:
            print(f"[KO] '{x}' not installed")
            module_not_found = True

    if module_not_found:
        print("All required modules were not found!")
        return

    try:
        plt = importlib.import_module("matplotlib.pyplot")
        np = importlib.import_module("numpy")
    except (ModuleNotFoundError, ImportError):
        print("Found broken modules!")
        return

    pd = mods["pandas"]
    data = np.random.rand(1000, 5)
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

    print(
        "\nAnalyzing Matrix data...",
        "Processing 1000 data points...",
        "Generating visualization...",
        sep="\n"
    )

    plt.hist(df['A'], bins=20)
    plt.title('Histogram of Column A')
    plt.savefig('matrix_analysis.png')
    plt.show()

    print(
        "\nAnalysis complete!",
        "Results saved to: matrix_analysis.png",
        sep="\n"
    )


if __name__ == "__main__":
    main()

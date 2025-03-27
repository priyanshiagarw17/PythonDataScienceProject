from DataAnalyzer import Analyzer

Analysis = Analyzer(r"C:\Users\user\OneDrive\Desktop\Student Mental health.csv")

Analysis.__init__(file_path=r"C:\Users\user\OneDrive\Desktop\Student Mental health.csv")
Analysis.show_basic_info()
Analysis.rename()
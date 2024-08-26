from os import system
print("Taki: Hey, how can I help you?")
msg = input("You: ")
if "predict" in msg:
    print("Taki: Sure, I can help you with that. Currently I can predict")
    print("Taki: Stock Market Prediction")
    print("Taki: Area Safety Prediction")
    print("Taki: Lift Maintenance Prediction")
    print("Taki: Bank Loan Prediction")
    print("Taki: Plantation Prediction")
    print("Taki: Heart Attack Prediction")
    print("Taki: Sales Prediction")
    print("Taki: Crop Yield Prediction")
    print("Taki: Feature Acceptance Prediction")
    print("Taki: Cab Fare Prediction")
    msg = input("You: ")
    if "stock" in msg or "Stock" in msg:
        print("Taki: Connecting you to Stock Market Prediction Service, please hold...")
        system("python StockMarketPrediction.py")
    if "area" in msg or "Area" in msg or "safety" in msg or "Safety" in msg:
        print("Taki: Connecting you to Area Safety Prediction Service, please hold...")
        system("python AreaSafetyPrediction.py")
    if "lift" in msg or "Lift" in msg:
        print("Taki: Connecting you to Lift Maintenance Prediction Service, please hold...")
        system("python LiftMaintenancePrediction.py")
    if "bank" in msg or "Bank" in msg:
        print("Taki: Connecting you to Bank Loan Prediction Service, please hold...")
        system("python BankLoanPrediction.py")
    if "plant" in msg or "Plant" in msg:
        print("Taki: Connecting you to Plantation Prediction Service, please hold...")
        system("python PlantationPrediction.py")
    if "heart" in msg or "Heart" in msg:
        print("Taki: Connecting you to Heart Attack Prediction Service, please hold...")
        system("python HeartAttackPrediction.py")
    if "sales" in msg or "Sales" in msg:
        print("Taki: Connecting you to Sales Prediction Service, please hold...")
        system("python SalesPrediction.py")
    if "crop" in msg or "Crop" in msg:
        print("Taki: Connecting you to Crop Yield Prediction Service, please hold...")
        system("python CropYieldPrediction.py")
    if "feature" in msg or "Feature" in msg:
        print("Taki: Connecting you to Feature Acceptance Prediction Service, please hold...")
        system("python FeatureAcceptancePrediction.py")
    if "cab" in msg or "Cab" in msg:
        print("Taki: Connecting you to Cab Fare Prediction Service, please hold...")
        system("python CabFarePrediction.py")
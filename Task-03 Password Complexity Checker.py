import re

def assess_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    
    if re.search(r'[A-Z]', password):
        score += 1
    
    if re.search(r'[a-z]', password):
        score += 1
    
    if re.search(r'[0-9]', password):
        score += 1
    
    if re.search(r'[!@#$%^&*()\-_=+{};:,.<>?]', password):
        score += 1
    
    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Moderate password"
    else:
        return "Weak password"

def main():
    print("Password Strength Checker")
    print("-------------------------")
    
    while True:
        password = input("\nEnter a password to assess its strength (type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("\nExiting program.")
            break
        
        strength = assess_password_strength(password)
        print(f"\nPassword strength: {strength}\n")

if __name__ == "__main__":
    main()

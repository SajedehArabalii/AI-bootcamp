import os
import json

# Main execution loop of the program
def main():
    """
    Responsibilities:
    - Load the JSON database from disk
    - Extract the list of karvands (participants)
    - Continuously show a menu until the user exits
    - Route the user's choice to the correct function
    """
    
    database = load_data()# Load JSON file into memory
    karvands = database['karvands']# Extract the list of karvands

    print("Welcome to karvand management.")

    # Menu:
    while True:
        choice = get_choice(
            "1-Add karvand\n2-Show karvand\n3-Search by ID\n4-Search by skills\n5-Edit karvand\n6-Delete karvand\n7-General Report\n8-Exit\nYour choice: "
        )
        match choice:
            case "1":
                add(karvands, database)
            case "2":
                show(karvands)
            case "3":
                search_by_id(karvands)
            case "4":
                search_by_skill(karvands)
            case "5":
                edit(karvands, database) 
            case "6":
                delete(karvands, database) 
            case "7":
                report(karvands) 
            case "8":
                print("Goodbye!")
                break

# Handles menu input validation
def get_choice(prompt):
    """
    Purpose:
    - Ensure the user enters a number
    - Ensure the number is between 1 and 6
    - Prevent the program from crashing due to invalid input
    """
    while True:
        try:
            choice = input(prompt)

            # Numeric range
            if 1 <= int(choice) <= 8:
                return choice
            else:
                print("\tEnter a number from 1 to 8.")
        
        # Handles ValueErrors
        except ValueError:
            print("\tEnter a number")

# Add a new karvand to the system
def add(karvands, database):
    """
    Process:
    1. Collect basic information
    2. Collect education details (nested dictionary)
    3. Collect multiple skills (list of dictionaries)
    4. Add the new record to the karvands list
    5. Save the updated database to disk
    """
    print("Enter information of karvand")

    # Data containers
    karvand = {}
    education = {}
    skills = []

    # Basic info
    karvand["id"] = assign_ID(karvands)
    karvand["full_name"] = input("Full name: ")
    karvand["email"] = input("Email: ")
    karvand["city"] = input("City: ")

    # Education dictionary
    education["degree"] = input("Degree: ")
    education["field"] = input("Field: ")

    # Collect multiple skills until the user gives an empty skill name
    # Now your add function logic becomes very clean:
    while True:
        name = input("Skill (or press enter to finish): ")
        if name == "":
            break
        skills.append(get_skill(name))

    # Attach nested data to the main record
    karvand["education"] = education
    karvand["skills"] = skills

    # Add the new participant to the list
    karvands.append(karvand)

    # Persist changes to disc
    save_data(database)

    print("\tAdding karvand was successful.")

# Display all registered karvands
def show(karvands):
    """
    Key ideas:
    - Defensive programming using dict.get()
    - Prevents crashes if a field is missing in JSON
    - Properly unpacks nested dictionaries and lists
    """

    # Check if karvands is empty
    if not karvands:
        print("No karvands found in the list.")
        return
    
    print("=========Registered Karvands==========")
    
    # Use .get(key, default) so that if a key is missing from JSON, the program does not crash
    # Enumerate gives index numbers for display
    for index, karvand in enumerate(karvands, start=1):

        # Basic info
        print(f"\t[{index}] ID: {karvand.get('id')} | {karvand.get('full_name','No Name')}")
        print(f"\tEmail:{karvand.get('email','N/A')}")
        print(f"\tCity: {karvand.get('city','N/A')}")

        # Unpacking education
        edu = karvand.get("education", {})
        degree = edu.get("degree", "N/A")
        field = edu.get("field", "N/A")
        print(f"\tEducation: {degree} in {field}")

        # Unpacking skills
        skills = karvand.get("skills", [])
        if skills:
            print("\tSkills:")
            for skill in skills:
                name = skill.get("name", "N/A")
                level = skill.get("level", "N/A")
                score = skill.get("score", "N/A")
                print(f"\t  - {name} ({level}) | Score: {score}")

        else:
            print("\tSkills: None listed")

    print("=======================================")

# Search for a specific karvand using their ID
def search_by_id(karvands):
    """
    Finds and displays a single participant matching the entered ID.
    """

    try:
        search_id = int(input("Enter the ID of the karvand to search for: "))
    except ValueError:
        print("\tPlease enter a valid numeric ID.")
        return

    target_karvand = None

    # Search
    for karvand in karvands:
        if karvand.get("id") == search_id:
            target_karvand = karvand
            break

    # If found
    if target_karvand:
        print(f"\n========== Karvand Details (ID: {search_id}) ==========")
        print(f"Name: {target_karvand.get('full_name', 'No Name')}")
        print(f"Email: {target_karvand.get('email', 'N/A')}")
        print(f"City: {target_karvand.get('city', 'N/A')}")

        edu = target_karvand.get("education", {})
        print(f"Education: {edu.get('degree', 'N/A')} in {edu.get('field', 'N/A')}")

        skills = target_karvand.get("skills", [])

        if skills:
            print("Skills:")
            for skill in skills:
                print(
                    f"  - {skill.get('name', 'N/A')} "
                    f"({skill.get('level', 'N/A')}) "
                    f"| Score: {skill.get('score', 'N/A')}"
                )
        else:
            print("Skills: None listed")

        print("=" * 50)

    else:
        print(f"\nNo karvand found with ID {search_id}")

# Search for karvands who have a specific skill
def search_by_skill(karvands):
    """
    Finds and displays all karvands possessing a specific skill.
    Performs case-insensitive matching.
    """
    search_query = input("Enter the skill name to search for: ").strip().lower()
    
    if not search_query:
        print("Invalid search input.")
        return

    found_any = False
    print(f"\n--- Search results for skill: '{search_query}' ---")
    
    for karvand in karvands:
        skills = karvand.get("skills", [])
        for skill in skills:
            skill_name = skill.get("name", "").strip().lower()
            
            # Match found
            if skill_name == search_query:
                found_any = True
                print(f"ID: {karvand.get('id', 'N/A')} | Name: {karvand.get('full_name', 'No Name')} | City: {karvand.get('city', 'N/A')}")
                print(f"  - Skill: {skill.get('name')} | Level: {skill.get('level', 'N/A')} | Score: {skill.get('score', 'N/A')}")
                print("-" * 40)
                break  # Stop checking other skills of this participant to avoid double-printing if they duplicated it
                
    if not found_any:
        print("No participants found with that skill.")
    print("-------------------------------------------\n")

# Edit an existing karvand record
def edit(karvands, database):
    """
    Steps:
    1. Search for a participant by ID
    2. Allow editing of three sections separately:
    - Basic Info
    - Education
    - Skills
    3. Blank input keeps the current value
    4. Save changes immediately
    """

    # Loop unitl a valid ID is found or user quits
    while True:
        try:
            search_id = int(input("Enter the ID of the karvand you want to edit: "))
            target_karvand = None

            # Linear search
            for karvand in karvands:
                if karvand["id"] == search_id:
                    target_karvand = karvand
                    break

            # If not found
            if target_karvand is None:
                choice = input("Karvand not found, do you want to continue? (y/n): ")
                if choice.lower() != "y":
                    return
            else:
                break

        except ValueError:
            print("Enter karvand ID as a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

    print(f"\n--- Editing {target_karvand['full_name']} (ID: {search_id}) ---")

    #---------------------------
    # 1. BASIC INFO UPDATE
    #---------------------------
    print("\nDo you want to edit basic information (Name, Email, City)? (y/n)")
    if input().lower() == "y":
        print("Leave blank and press Enter to keep current value.")

        name = input(f"Full Name [{target_karvand.get('full_name', '')}]: ")
        if name:
            target_karvand["full_name"] = name

        email = input(f"Email [{target_karvand.get('email', '')}]: ")
        if email:
            target_karvand["email"] = email

        city = input(f"City [{target_karvand.get('city', '')}]: ")
        if city:
            target_karvand["city"] = city

    #-----------------------------
    # 2. EDUCATION UPDATE
    #-----------------------------
    print("\nDo you want to edit education details? (y/n)")
    if input().lower() == "y":
        print("Leave blank and press Enter to keep current value.")

        if "education" not in target_karvand:
            target_karvand["education"] = {"degree": "", "field": ""}

        edu = target_karvand["education"]

        degree = input(f"Degree [{edu.get('degree', '')}]: ")
        if degree:
            edu["degree"] = degree

        field = input(f"Field [{edu.get('field', '')}]: ")
        if field:
            edu["field"] = field
    #----------------------------
    # 3. SKILLS UPDATE
    #----------------------------
    print("\nDo you want to edit skills? (y/n)")

    if input().lower() == "y":

        print("Updating skills list...")
        new_skills = []

        while True:
            s_name = input("Skill Name (leave blank to finish): ")
            if not s_name:
                break

            new_skills.append(get_skill(s_name))

        if new_skills:
            target_karvand["skills"] = new_skills



    save_data(database) # Auto-save updates
    print("\n\tUpdate successful!")

# Delete a participand by ID
def delete(karvands, database):
    """
    Process:
    1. Search for participant
    2. Ask confirmation to prevent accidental deletion
    3. Remove from list
    4. Save database
    """
    while True:
        try:
            search_id = int(input("Enter the ID of the karvand you want to delete: "))
            target_karvand = None

            # Search for matching ID
            for karvand in karvands:
                if karvand["id"] == search_id:
                    target_karvand = karvand
                    break

            if target_karvand is None:
                choice = input(
                    "Karvand not found. Do you want to try another ID? (y/n): "
                )
                if choice.lower() != "y":
                    return 
            else:
                break

        except ValueError:
            print("Enter karvand ID as a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return
    # Safety confirmation
    confirm = input(
        f"Are you sure you want to delete {target_karvand['full_name']} (ID: {search_id})? (y/n): "
    )

    # Remove from list
    if confirm.lower() == "y":
        karvands.remove(target_karvand)
        save_data(database)
        print(f"\n\tID {search_id} has been successfully deleted!")
    else:
        print("\n\tDeletion cancelled.")

# Generate analytical statistics about the stored data
def report(karvands):
    """
    Calculations include:
    - Total number of karvands
    - Total number of registered skills
    - Average score across all skills
    - List of registered cities (unique)
    - List of unique skills
    """ 
    if not karvands:
        print("\n\tNo data available to generate a report.")
        return

    print("\n================ GENERAL REPORT ================")
    
    #------------------------------------------------
    # 1. Total participants 
    #------------------------------------------------
    total_students = len(karvands)
    print(f"Total Registered Karvands: {total_students}")

    #-------------------------------------------------
    # 2. Total registered skills & Unique skills 
    #-------------------------------------------------
    total_skills_count = 0
    unique_skills = set()
    total_score = 0
    score_count = 0

    for k in karvands:
        skills = k.get("skills", [])
        for skill in skills:
            total_skills_count += 1
            
            # Extract skill name for unique list
            skill_name = skill.get("name", "").strip().title()
            if skill_name:
                unique_skills.add(skill_name)
            
            # Extract score for average calculation
            try:
                score = float(skill.get("score", 0))
                total_score += score
                score_count += 1
            except (ValueError, TypeError):
                continue

    print(f"Total Registered Skills: {total_skills_count}")

    #---------------------------------------------------
    # 3. Average skill score 
    #---------------------------------------------------
    if score_count > 0:
        avg_score = total_score / score_count
        print(f"Average Skill Score: {avg_score:.2f} (based on {score_count} graded skills)")
    else:
        print("Average Skill Score: N/A (no numeric scores available)")

    #-----------------------------------------------------
    # 4. List of registered cities 
    #-----------------------------------------------------
    unique_cities = set()
    for k in karvands:
        city = k.get("city", "").strip().title()
        if city:
            unique_cities.add(city)
            
    print(f"\nRegistered Cities ({len(unique_cities)}):")
    if unique_cities:
        print("  - " + ", ".join(sorted(unique_cities)))
    else:
        print("  - None")
    #-----------------------------------------------------
    # 5. List of unique skills
    #-----------------------------------------------------
    print(f"\nUnique Registered Skills ({len(unique_skills)}):")
    if unique_skills:
        print("  - " + ", ".join(sorted(unique_skills)))
    else:
        print("  - None")
        
    print("================================================\n")

#Collect and validate skill
def get_skill(name):
    level = input(f"Level for {name}: ")
    
    while True:
        try:
            score = int(input(f"Score for {name} (0-100): "))
            if 0 <= score <= 100:
                return {"name": name, "level": level, "score": score}
            print("\tScore must be between 0 and 100.")
        except ValueError:
            print("\tPlease enter a valid integer.")

# Write the database dictionary to disc as JSON
def save_data(data):
    """
    Important responsibilities:
    - Create data folder if it does not exist
    - Serialize Python dictionary to JSON
    - Save changes permanently
    """
    folder_path = "data"
    file_path = os.path.join(folder_path, "database.json")
    
    try:
        os.makedirs(folder_path, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("\n\tData saved successfully to data/database.json!")
    except Exception as e:
        print(f"Error saving data: {e}")

# Load the database JSON file
def load_data():
    """
    If the file does not exist:
    - Create the folder
    - Initialize a default database structure

    If loading fails:
    - Return default empty structure
    """
    file_path = os.path.join("data", "database.json")
    default_data = {
        "bootcamp": {
            "title": "Karvand Python",
            "year": 2026
        },
        "karvands": []
    }
    
    if not os.path.exists(file_path):
        os.makedirs("data", exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
        return default_data

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading database file: {e}. Starting with empty data.")
        return default_data

# Generate a unique ID for new karvands
def assign_ID(karvands):
    """
    Logic:
    - If list is empty → start at 1
    - Otherwise → take the highest ID and add 1
    """
    if not karvands:
        new_id = 1
    else:
        # new_id = max(k["id"] for k in karvands) + 1
        new_id = max(k.get("id", 0) for k in karvands) + 1
    return new_id


if __name__ == "__main__":
    main()

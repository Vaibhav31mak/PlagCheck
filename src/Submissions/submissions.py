import os
import json

def detect_language(filename):
    ext = filename.split('.')[-1]
    return {
        'cpp': 'C++',
        'py': 'Python',
        'java': 'Java',
        'c': 'C',
        'cs': 'C#'
    }.get(ext, 'Unknown')

def parse_filename(filename):
    name = os.path.splitext(filename)[0]
    parts = name.split('_')
    if len(parts) >= 2:
        return parts[0], parts[1]  # username, problem
    return "unknown", "unknown"

def collect_submissions(folder_path):
    submissions = []
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Directory not found: {folder_path}")
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            username, problem = parse_filename(file)
            language = detect_language(file)
            submissions.append({
                "username": username,
                "problem": problem,
                "language": language,
                "code": code
            })
    return submissions

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Data successfully saved to {file_path}")

def main():
    try:
        # Assumes subs folder is inside src/Submissions/
        subs_folder = os.path.join(os.path.dirname(__file__), "subs")
        output_path = os.path.join(os.path.dirname(__file__), "submissions.json")

        data = collect_submissions(subs_folder)
        save_to_json(data, output_path)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

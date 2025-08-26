import json
import os



class JsonUtility:
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    save_directory = os.path.join(parent_dir, "Data")
    save_file = "tasks.json"
    save_file_X = "taskboxes.json"
    complete_save_file_path = os.path.join(save_directory, save_file)
    complete_save_file_path_X = os.path.join(save_directory, save_file_X)


    def __init__(self):
        """Initializes the JsonUtility class."""
        specified_save_directory = JsonUtility.get_save_directory()

        

    @staticmethod
    def load_json(file_path):
        """Load JSON data from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_json(data, file_path):
        """Save JSON data to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)



    @staticmethod
    def get_save_directory(i=0):
        """Get the directory where JSON files are saved."""

        #stop condition if reccursivity goes too deep
        if i > 2:
            print("Error: Could not find a valid save directory after 3 attempts.")
            return None

        # get the config file path
        config_path = os.path.join(JsonUtility.parent_dir, "config.json")
        # print("========> " + config_path)

        # default values for if there is an issue with default config file
        save_directory = "test"
        save_file = JsonUtility.save_file
        save_file_X = JsonUtility.save_file_X
        complete_save_file_path = JsonUtility.complete_save_file_path
        complete_save_file_path_X = JsonUtility.complete_save_file_path_X

        # Resilience about config file + default values settings for config file (is this considered a fixture?)
        with open(config_path, 'r', encoding='utf-8') as file:
            cfg_content = file.read()
            # print("CFG : " + cfg_content + " " + str(len(cfg_content)))
            if len(cfg_content) == 0:
                print(f"Config file is empty: {config_path}")
            else:
                with open(config_path, 'r', encoding='utf-8') as file:
                    Config_json = json.load(file)
                save_directory = Config_json.get("saveTo")
                save_file = Config_json.get("save_name")
                save_file_X = Config_json.get("save_name_X")
                complete_save_file_path = os.path.join(save_directory, save_file)
                complete_save_file_path_X = os.path.join(save_directory, save_file_X)

        # If the save directory is not set or is invalid, use default values
        if save_directory in ["", None, "test"]:
            # Use default values if config is missing or invalid
            save_directory = os.path.join(JsonUtility.parent_dir, "Data")
            save_file = "tasks.json"
            save_file_X = "taskboxes.json"
            complete_save_file_path = os.path.join(save_directory, save_file)
            complete_save_file_path_X = os.path.join(save_directory, save_file_X)
            if not os.path.exists(save_directory):
                print(f"Creating save directory: {save_directory}")
                os.makedirs(save_directory)
            JsonUtility.set_save_directory(save_directory, save_file, save_file_X, complete_save_file_path, complete_save_file_path_X)
            with open(complete_save_file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)
            with open(complete_save_file_path_X, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)
            #if there was an issue, reccursively retry with all config set by default
            return JsonUtility.get_save_directory(i+1)
        else:
            # If the save directory is valid, set the class variables and return complete save path
            JsonUtility.save_directory = save_directory
            JsonUtility.save_file = save_file
            JsonUtility.save_file_X = save_file_X
            JsonUtility.complete_save_file_path = complete_save_file_path
            JsonUtility.complete_save_file_path_X = complete_save_file_path_X
            # print(f"Save set to: {JsonUtility.complete_save_file_path}")
            # print(f"Save set to: {JsonUtility.complete_save_file_path_X}")
            return [complete_save_file_path, complete_save_file_path_X]


    @staticmethod
    def set_save_directory(dir, name, name_X, complete, complete_X):
        """Set the directory where JSON files are saved."""
        config = {
            "saveTo": dir,
            "save_name": name,
            "save_name_X": name_X,
            "complete_path": complete,
            "complete_path_X": complete_X
        }
        config_path = os.path.join(JsonUtility.parent_dir, "config.json")
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4, ensure_ascii=False)

    @staticmethod
    def save_to_file(data, filename):
        """Save data to a JSON file."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_file(filename):
        """Load data from a JSON file."""
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

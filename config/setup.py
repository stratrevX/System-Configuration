# Preinstalled Python Libraries

from pathlib import Path

# Constant
# ~ Desired Directory Path: C:\Users\%CURRENTUSER%\.config\
directory_path = Path(Path.home() / '.config/') #C:\Users\<current-user> in Windows, #~/home/<current-user>
print(f"desired directory path: {directory_path}")

if directory_path is False:
    print(f"config directory was not found at: {directory_path}")
    directory_path.mkdir(parents=True, exist_ok=True)
else:
    print("config directory found.")
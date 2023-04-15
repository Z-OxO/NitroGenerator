# NitroGenerator

<!DOCTYPE html>
<html lang="en>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Nitro Generator</h1>
    <p>A simple Python script that generates random Discord Nitro gift codes.</p>
    <h2>Usage</h2>
    <p>1. Install the required dependencies:</p>
    <code>pip install colorama</code>
    <br>
    <code>pip install random</code>
    <br>
    <code>pip install time</code>
    <p>2. Run the script:</p>
    <code>python nitrogenerator.py</code>
    <p>3. Select an option from the menu:</p>
    <ul>
      <li>1: Generator - Generates Nitro gift codes</li>
      <li>2: Hit - Displays previously found valid Nitro gift codes</li>
      <li>3: Exit - Exits the script</li>
    </ul>
    <h2>Functionality</h2>
    <p>The Nitro Generator script generates random Discord Nitro gift codes and displays them in the console. The script also saves any valid Nitro gift codes that are generated to a text file, which can be accessed from the menu option "Hit".</p>
    <p>The generator function prompts the user to input the number of tests they would like to run. For each test, the script generates a 17-character random string that is appended to the URL "http://discord.gift/". The script then displays the URL in the console and checks if the URL is valid by generating a random number between 1 and 100. If the generated number matches a pre-determined valid number, the script saves the URL to the "hit.txt" file and displays the URL in green in the console.</p>
    <p>The hit function reads and displays the contents of the "hit.txt" file, which contains any previously found valid Nitro gift codes.</p>
  </body>
</html>

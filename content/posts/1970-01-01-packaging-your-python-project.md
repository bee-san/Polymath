---
title: Packaging your Python Project
slug: packaging-your-python-project
date_published: 1970-01-01T00:00:00.000Z
date_updated: 2020-07-18T13:17:32.000Z
draft: true
---

I was looking to package my project, Ciphey, for operating systems and for managers that isn't PyPi. Unforuantely, there seemed to be very little information on the web about this.

This is a guide on packaging your Python project for:

- PyPi
- HomeBrew
- Windows Package Manager
- Arch User Respository

# Ideas

Publish each one seperately, and include a pdf containing the full book

Include github actions for these

Explain semenatic versioning

# Semantic Versioning

Semantic Versioning is a system defining how to write version numbers. The 3 numbers are:

    Major.Minor.Bugs

If you have fixed some bugs, increment the bugs counter.

If you have added a minor feature, increment the minor counter.

If you have done something major, increment the major counter.

We can signify whether a release is still being rested or not by adding "rc" (release candidate) to the end of the version. "5.0.0rc1" signifies "release canidate 1" which means this is the first public testing release of version 5.0.0.

# PyPi

The traditional method of using Setuptools is outdated and old. There's a new cowboy in town, and their name is Poetry.

Poetry creates a `pyproject.yml` file, which is the [successor](https://www.python.org/dev/peps/pep-0517/) to the 3-file Setuptools sytem.

You should use Poetry because:

- Instead of 3 files, it is now 1 file
- That 1 file is yaml, which means you don't have to cry reading weirdly formatted Python code used as a replacement for yaml
- You can seperate dev & normal dependencies, so users only install the dependencies they need to run the app
- It's physically easier to build and upload to PyPi
- And a host of other things

Install poetry with `pip3 install poetry`.

Navigate to your projects directory and run the command `poetry init`.

This will generate a `pyproject.toml` file. This file contains everything PyPi needs to upload your project, and allow other users to download it.

Let's run through the sections in this new file, and fill then out as we go.

**[tool.poetry]**

This section relates to the metadata of your project.

The name, description, version etc.

To add a new variable to a .toml file, write it as if it were python `name = "project name"`.

The most important ones we'll want are:

- Name

What is the name of the project?

    name = "Ciphey`

- Version

The semantic version number.

    version = "5.0.0rc6"

- Description

Short one line description.

    description = "Automated decryption tool"

- Authors

A list containing the authors name and email address. In the format of `authors = ["brandon <brandon@fake.com>"]`

- License

What license does the project use?

    license = "MIT"

- readme

The name of the `README.md` file, in the same directory as `pyproject.toml`.

    readme = "README.md"

Here is what Ciphey's Pyproject looks like:

    [tool.poetry]
    name = "ciphey"
    version = "5.0.0rc4"
    description = "Automated Decryption Tool"
    authors = ["Brandon <brandon@skerritt (dot) blog>"]
    license = "MIT"
    documentation = "https://docs.ciphey.online"
    exclude = ["tests/hansard.txt"]
    readme = "README.md"

To find out what else you can include, check out the [Poetry documentation.](https://python-poetry.org/docs/pyproject/)

**[tool.poetry.dependencies]**

A list of all the dependnecies your project uses. Don't worry! You don't have to manually add them to te list.

Run the command `poetry add <dependency>` to add a dependency to your project, and Poetry will automatically add it to your project.

For example, to add `rich` we would write `poetry add rich`.

**[tool.poetry.dev-dependencies]**

The dependencies the developers of your tool rely on. To add the testing library Pytest, write `poetry add --dev pytest`.

**[tool.poetry.scripts]**

This is the 2nd most important part! As it contains an entry point. When a user installs your package, you'd probably like them to be able to run `package` in their terminal and use your package.

For a folder called Ciphey with a file named Ciphey.py with a function called main(), we would write:

    ciphey = 'ciphey.ciphey:main'

When the user runs the command `ciphey`, it actually runs the main function of the file ciphey of the folder ciphey.

For a more detailed explanation, [check this out.](https://amir.rachum.com/blog/2017/07/28/python-entry-points/)

## Poetry Run

`poetry run` runs our script, but includes the `pyproject.toml` file. It executes the given command inside of a virtual environment, essentially it allows us to test our project in the same way a user might run our program.

## Poetry Install

`Poetry install` installs our program and all its dependencies. Essentially, we can test exactly what our users will do when they install the project for themselves.

## Poetry Update

`poetry update` updates our dependencies.

## Poetry Build

Now onto the most important commands. `Poetry build` builds our project, which means it generates some files that other users can install and use on their system.

## Poetry publish

`Poetry Publish` will publish the package to PyPi for us. All we need to do is enter a username / password.

And just like that, our project is now on PyPi for the whole world to download!

## Automatic Uploading using github actions

# Windows Package Manager (WinGet)

There are 3 steps to submitting your app to WinGet.

1. Turning your project into an EXE
2. Create a manifest file
3. Create a pull request on GitHub

## Turning your project into an EXE

Windows requires an exe file for Python projects. Don't fret! Turning your project into a exe file isn't that difficult.

Download Pyinstaller, and then create an `entry point` in the root directory.

An entry point is a python file that when ran, will run the program. So for instance:

    Ciphey/
    |-entry_point.py
    |-ciphey/
    |----main.py

Here the project code is in `ciphey/`. To run the program, we'd have to run `python3 ciphey/main.py`. 

This is the typical file structure of a project. We have README.md and similar in the root, and all the source code into a sub-directory.

We need to create a program that calls our program using an entry point. The entry point is a function which runs the program.

If you have a `setup.py` or `pyproject.yml`, you may already have entry points defined in them.

In `entry_point.py`, we'd write:

    from ciphey.__main__ import main
    
    if __name__ == '__main__':
    	main()

Or however your entry point is defined.

Now, run Pyinstaller on the `entry_point.py` file. It will generate a new folder called `dist/`. If you are using the default Python `.gitignore` it will automatically disclude `dist/`. If not, please add it to the `.gitignore`!

Pyinstaller will also generate an `entry_point.spec` file in the root directory. This file contains a specification of how Pyinstaller should build your program.

Once built, run the program.

You will likely see some errors. Most likely bad imports. To fix this, define them in the spec file. There are a couple main lists in the spec file you should know about:

- Binaries

If you already hold a binary for a specific file / library (such as C++ compiled) then define the location here.

- Datas

If your program relies on .txt data, or anything that isn't a Python file define it here.

- Hidden Imports

Hidden imports look like `__import__`.  These types of imports are not visible to Pyinstaller's analysis, so to get around this define the imports in the Hidden imports section.

- Excludes

Exclude a package from Pyinstaller. I had an error with Setuptools, but since Setuptools isn't needed to run Ciphey I told Pyinstaller to exclude the entire package.

If you have edited the `.spec` file, you may want to delete the line from the `.gitignore` which states to ignore the file. Otherwise, all the hard work you've spent in getting Pyinstaller to work may be lost.

**One thing to note**. Pyinstaller only creates executables for the system you are on. You cannot build a Windows .exe from Linux. You have to be on the system you are trying to build for. Pyinstaller can create these binaries (assuming you own the operating systems for them):

- Windows .exe
- Mac OS' .app
- Linux's Binary Files

Once built and packaged, running the executable on Windows / Mac will bring up the Terminal (assuming you do not have any GUI). If you do, it will bring up the GUI.

Pyinstaller packages an entire Python intrepreter with the binary, So do not worry about the user having Python installed.

## Manifest File

Now we have an exe. I would suggest converting to MSIX.

Exes are cool and all, but they're not really package manager matieral. Winget with an .exe is a glorified Softonic / CNET Software. MSIX gives us the real power to:

- Automatically update the app
- Uninstall cleanly
- Understand what dependencies are required

So in short, if we use an .exe it is just a glorified Software downloader. If we use .msix it is more of a package mamnager.

Below is the `manifest.yml` file for Ciphey. 

    Id: Ciphey.Ciphey 
    Publisher: Ciphey
    Name: Ciphey 
    Version: 5
    AppMoniker: Ciphey
    MinOSVersion: 10.0.0.0
    Description: Automated Decryption Tool
    Homepage: https://www.github.com/ciphey/ciphey
    License: MIT
    LicenseUrl: https://opensource.org/licenses/MIT 
    InstallerType: exe
    Installers:
      - Arch: x64
        Url: https://statics.teams.cdn.office.net/production-windows-x64/1.3.00.4461/Teams_windows_x64.exe
        Sha256: 712f139d71e56bfb306e4a7b739b0e1109abb662dfa164192a5cfd6adb24a4e1
    ManifestVersion: 0.1.0

Ciphey's manifest file
Let's walk through quickly what each potentially confusing part is. I'll leave things like "Name" and "License" as they are self-explanatory.

- ID

This follows a `publisher.package` format. Your publishers name, and then the package name.

- App Moniker

What's the common name people search for your package with? For example "Visual Studio Code" can also be found with "vscode".

If you have a long package name and your users often shorten it, this will be helpful to you.

- MinOSVersion

What is the minimum version of Windows the app supports? `10.0.0.0` means Windows 10 and above.

- InstallerType

What type of installer do you have? If you followed along, you should have an .exe file.

- Installers

This details how to install your package.

1. Architecturue

What architecture does your project support? Examples include `arm, arm64, x86, x64 and neutral`. 

The ones you're probably after are either x86 or x64. x86 is for 32-bit operating systems, x64 is for 64-bit operating systems.

2. URL

What is the URL of the .exe installer for your project? Personally, I hosted this on GitHub.

3. SHA256

What is the SHA256 checksum of your .exe file? There's an article [here](https://kanguru.zendesk.com/hc/en-us/articles/235228027-SHA256-Checksum-Utilities) detailing how to calculate it.

- Manifest Version

Everytime you update this file, update the manifest version numbering using Semantic Versioning.

# Arch User Respository

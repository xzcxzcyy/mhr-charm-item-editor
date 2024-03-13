# mhr-charm-item-editor
A Charm/Item editor for Monster Hunter Rise. **Modified for getting all item id, so that you can easily find the id of a specific item name.**

There are currently 2 separate projects in this directory. **Only REFramework Version can export item with names.**

## Usage

Simply visit [generated item list](item_list/item.csv). If it is out of date and you prefer to generate a new list for your own, see below.

## REFramework Version

Refer to https://www.nexusmods.com/monsterhunterrise/mods/17 for how to install and use the original mod. Remember to use `.dll` built by this project instead (or the one in [Release](https://github.com/xzcxzcyy/mhr-charm-item-editor/releases)). The original project does not export items with names (id and amount only).

By default it supports all languages supported by the game, although *quality of translation and implementation may vary across languages*.

Afterwards, **create a new game** in Monster Hunter Rise to avoid messing up your own save. In the new save, use this mod to add all items x1000, and then click export to get an `item.json` file. Use this [convert python script](item_list/convert.py) to get a `.csv` file.

## Building REFramework DLL Project

The project depends on a couple libraries. Package are listed in `vcpkg.json`. Visual Studio 2022 shall manage them for you automatically. Simply double click `RisePCItemEditor.sln` to open the project in Visual Studio, and build the project `RiseCharmEditorREF` **in Release, x64**. The post-build program will try to install `.dll` file to `C:\Program Files (x86)\Steam\steamapps\common\MonsterHunterRise\reframework\plugins`. Modify or disable this option in project setting if it does not meet your need.

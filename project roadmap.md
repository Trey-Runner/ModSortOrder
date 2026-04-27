# ModSortOrder Project Roadmap

- [x] Create Title for project DONE
- [x] Create Description of project DONE
- [x] Create README DONE
- [x] Create LICENSE DONE
- [x] Set up project file structure (main.py, steam_api.py, sorter.py) DONE

---

## Steam Collection Integration

- [x] Accept Steam Workshop collection ID input DONE
- [x] Fetch mod IDs from collection using Steam API DONE
- [x] Fetch mod details (title, ID) DONE
- [x] Add safety checks for invalid/private collections DONE
- [x] Prevent crashes on missing API fields DONE
- [x] Skip invalid or deleted Workshop items DONE

---

## Sorting System

- [x] Implement keyword-based priority sorting DONE
- [x] Prioritize frameworks over asset mods DONE
- [x] Group DLC and core game at top DONE
- [x] Add fallback sorting (alphabetical) DONE

---

## Testing Phase

- [ ] Test with one valid public collection ID
- [ ] Confirm mod_ids returns populated list
- [ ] Confirm mod titles display correctly
- [ ] Confirm sorting order matches priority rules
- [ ] Add debug output for mod_ids if needed

---

## Environment Setup

- [ ] Clone repository to local machine
- [ ] Open project in VS Code
- [ ] Install dependencies (requests)
- [ ] Run main.py successfully

---

## Next Core Improvements

- [ ] Parse local RimWorld mod files (About.xml)
- [ ] Implement dependency-based sorting (loadAfter/loadBefore)
- [ ] Detect missing dependencies
- [ ] Detect incompatible mods

---

## Output Improvements

- [ ] Export sorted mod list to file (txt or json)
- [ ] Improve terminal display formatting
- [ ] Add priority labels in output

---

## Future Features

- [ ] Add GUI interface
- [ ] Auto-detect installed mods from Steam directory
- [ ] Support multiple collections
- [ ] Save/load user configurations

---

## Immediate Next Step

Test program using a real Steam Workshop collection ID and verify output.

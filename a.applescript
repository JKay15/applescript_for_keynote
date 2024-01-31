on run argv
    -- ???????????
    repeat with filepath in argv
        tell application "System Events"
        -- set filepath to text returned of (display dialog "give the file path?" default answer "")
        -- delay 1
        tell application "Keynote" to activate
            tell process "Keynote"
                set frontmost to true

                click menu item 3 of menu 1 of menu bar item 3 of menu bar 1
                delay 0.5

                keystroke "g" using {command down, shift down}
                delay 0.5

                keystroke filepath
                delay 0.5

                keystroke return
                delay 0.5
                keystroke return
                delay 2
                click menu item 1 of menu 1 of menu item 18 of menu 1 of menu bar item 3 of menu bar 1  
                delay 0.1
                keystroke return 
                delay 0.1
                keystroke return 
                delay 1
                keystroke "q" using {command down}
            end tell
        end tell
    end repeat
    -- set filepath to item 1 of argv
    -- tell application "System Events"
    --     -- set filepath to text returned of (display dialog "give the file path?" default answer "")
    --     -- delay 1
    --     tell application "Keynote" to activate
    --     tell process "Keynote"
    --         set frontmost to true

    --         click menu item 3 of menu 1 of menu bar item 3 of menu bar 1
    --         delay 0.5

    --         keystroke "g" using {command down, shift down}
    --         delay 0.5

    --         keystroke filepath
    --         delay 0.5

    --         keystroke return
    --         delay 0.5
    --         keystroke return
    --         delay 2
    --         click menu item 1 of menu 1 of menu item 18 of menu 1 of menu bar item 3 of menu bar 1  
    --         delay 0.1
    --         keystroke return 
    --         delay 0.1
    --         keystroke return 
    --         delay 1
    --         keystroke "q" using {command down}
    --     end tell
    -- end tell
end run





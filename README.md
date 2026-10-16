# imprfct Keymap macOS

A personal JetBrains Rider keymap based on **ReSharper (macOS)**.

| Shortcut | Action |
| --- | --- |
| Cmd+W | Close the current tab |
| Cmd+1 through Cmd+9 | Select editor tab 1 through 9 |
| Option+W | Extend Selection |
| Option+Shift+W | Shrink Selection |

The original Cmd+F4, Option+Up, and Option+Down bindings are retained.
Cmd+1 through Cmd+9 are removed from tool-window actions to avoid conflicts.
Other shortcuts are inherited from ReSharper (macOS).

## Plugin installation

In Rider, open **Settings → Plugins → gear icon → Install Plugin from Disk** and choose `imprfct-keymap-macos-1.0.0.zip`.
Restart Rider if prompted, then select **imprfct Keymap macOS** in **Settings → Keymap**.
Requires Rider 2026.2 or newer and the bundled ReSharper Keymap plugin. Verified as compatible with Rider RD-262.10968.170 using JetBrains Plugin Verifier 1.410.

## Manual XML installation

Quit Rider. Copy [`imprfct Keymap macOS.xml`](resources/keymaps/imprfct%20Keymap%20macOS.xml) into `~/Library/Application Support/JetBrains/Rider<version>/keymaps/`.
Open Rider and select **imprfct Keymap macOS** in **Settings → Keymap**.

## Build

Run `python3 build.py`. The ZIP is written to `dist/`. The plugin contains only XML and SVG resources, plus the MIT license.

## Marketplace publishing

The archive is prepared for submission; it has not been published.
An author account, vendor profile, and developer agreement are required before submission. The license is MIT.
Publication is subject to JetBrains review. Local shortcut edits are not automatically published as updates.

[JetBrains custom keymaps documentation](https://www.jetbrains.com/help/rider/Configuring_Keyboard_and_Mouse_Shortcuts.html)

## License

MIT. See [LICENSE](LICENSE).

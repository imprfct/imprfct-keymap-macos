from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
resources = root / "resources"
version = ET.parse(resources / "META-INF/plugin.xml").findtext("version")
name = "imprfct-keymap-macos"
dist = root / "dist"
dist.mkdir(exist_ok=True)
destination = dist / f"{name}-{version}.zip"

def add_file(archive, name, data):
    entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    entry.compress_type = ZIP_DEFLATED
    entry.external_attr = 0o100644 << 16
    archive.writestr(entry, data)

jar = BytesIO()
with ZipFile(jar, "w") as archive:
    for path in sorted(resources.rglob("*")):
        if path.is_file():
            add_file(archive, str(path.relative_to(resources)), path.read_bytes())
    add_file(archive, "META-INF/LICENSE", (root / "LICENSE").read_bytes())
with ZipFile(destination, "w") as archive:
    add_file(archive, f"{name}/lib/{name}-{version}.jar", jar.getvalue())
print(destination)

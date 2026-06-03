import sharp from "sharp";
import path from "path";
import { fileURLToPath } from "url";
import fs from "fs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const src = path.join(root, "..", "LogoT.png");
const outIcon = path.join(root, "img", "logo-icon.png");
const outFavicon = path.join(root, "img", "favicon.png");

/** Checkerboard / white / light gray (not logo blue-cyan). */
function isBackdrop(r, g, b) {
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  const chroma = max - min;

  // Blue–cyan logo pixels
  if (chroma >= 22 && b >= 90 && b >= r - 8 && b >= g - 15) return false;
  if (r <= 70 && g <= 140 && b >= 150 && chroma >= 18) return false;

  // White fringe, checkerboard tiles, light gray
  if (max >= 185 && chroma <= 32) return true;
  if (max >= 250) return true;

  return false;
}

const { data, info } = await sharp(src)
  .ensureAlpha()
  .raw()
  .toBuffer({ resolveWithObject: true });

const { width, height } = info;
const visited = new Uint8Array(width * height);
const queue = [];

const idx = (x, y) => (y * width + x) * 4;
const push = (x, y) => {
  const i = y * width + x;
  if (x < 0 || y < 0 || x >= width || y >= height || visited[i]) return;
  const p = idx(x, y);
  if (!isBackdrop(data[p], data[p + 1], data[p + 2])) return;
  visited[i] = 1;
  queue.push(i);
};

// Flood-fill backdrop from image edges
for (let x = 0; x < width; x++) {
  push(x, 0);
  push(x, height - 1);
}
for (let y = 0; y < height; y++) {
  push(0, y);
  push(width - 1, y);
}

while (queue.length) {
  const i = queue.pop();
  const p = i * 4;
  data[p + 3] = 0;
  const x = (i % width);
  const y = Math.floor(i / width);
  push(x - 1, y);
  push(x + 1, y);
  push(x, y - 1);
  push(x, y + 1);
}

// Remove leftover white halo pixels
for (let p = 0; p < data.length; p += 4) {
  if (data[p + 3] === 0) continue;
  const r = data[p];
  const g = data[p + 1];
  const b = data[p + 2];
  if (isBackdrop(r, g, b)) data[p + 3] = 0;
}

const processed = sharp(data, {
  raw: { width, height, channels: 4 },
});

await processed
  .clone()
  .resize(512, 512, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .png({ compressionLevel: 9, adaptiveFiltering: true })
  .toFile(outIcon);

await processed
  .clone()
  .resize(32, 32, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .png({ compressionLevel: 9 })
  .toFile(outFavicon);

const stats = await sharp(outIcon).stats();
console.log("logo-icon: alpha channel ok =", stats.isOpaque === false);
console.log("logo-icon KB:", Math.round(fs.statSync(outIcon).size / 1024));

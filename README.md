# Kokemusu 公開ページ

https://koki25ando.github.io/kokemusu/ で公開している。

プライバシーポリシーの原稿は非公開リポジトリの `docs/play-store/privacy-policy.md`。直したら次で HTML を作り直してコミットする。

```bash
python3 build_privacy.py ../android/docs/play-store/privacy-policy.md > privacy/index.html
python3 build_privacy.py ../android/docs/play-store/privacy-policy-en.md en > privacy/en/index.html
```

英語版は `en/index.html`（日本語版と同じ構成。画面の画像は `img/en/`、Android 版の英語の画面）。日本語版を直したら英語版も合わせる。

紹介動画 `video/` は三野晃門様に外注した PR 動画（`marketing/pr_videos/三野晃門/`）をウェブ用に 720p・約4MB に書き出したもの。日本語版はテロップ入り、英語版はテロップなし版。

```bash
ffmpeg -i 元の動画.mp4 -vf scale=720:-2 -c:v libx264 -preset slow -crf 25 -pix_fmt yuv420p -c:a aac -b:a 96k -movflags +faststart video/kokemusu-pr.mp4
```

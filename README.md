# <img src="https://www.waifu.im/favicon.png" width="28" style="vertical-align:middle;" /> waifu_im.py

> Web-API for [waifu.im](https://waifu.im) browse and manage an archive of 4000+ anime images with tag filtering, NSFW support, and personal favourites.

## Quick Start
```python
from waifu_im import WaifuIm

waifu = WaifuIm()

# Optional — required for favourites and reports
waifu.login_with_token(token="your_token")

# Get a random image
print(waifu.get_random_image())
```

---

## Authentication

| Method | Description |
|--------|-------------|
| `login_with_token(token)` | Set bearer token for authenticated endpoints |

> Authentication is optional for browsing but required for managing favourites and reporting images.

---

## Images

| Method | Description |
|--------|-------------|
| `get_random_image(selected_tags, excluded_tags, is_nsfw, is_gif, orientation, is_many)` | Get one or many random images |
| `get_image_info(image)` | Get detailed info about a specific image |
| `get_tags_list(full)` | Get all available tags |
| `report_image(image, description, user_id)` | Report an image |

**Orientation options:** `LANDSCAPE`, `PORTRAIT`, `RANDOM`
```python
# Get a random GIF
waifu.get_random_image(is_gif=True)

# Get multiple images with a specific tag
waifu.get_random_image(selected_tags="waifu", is_many=True)

# Exclude a tag
waifu.get_random_image(excluded_tags="oppai")
```

---

## Favourites

| Method | Description |
|--------|-------------|
| `get_favourites(user_id, selected_tags, excluded_tags, is_nsfw, is_gif, order_by, orientation, is_many)` | Get your favourited images |
| `insert_favourite(image, user_id)` | Add an image to favourites |
| `delete_favourite(image, user_id)` | Remove an image from favourites |
| `toggle_favourite(image, user_id)` | Toggle favourite status |

**Order by options:** `FAVOURITES`, `UPLOADED_AT`, `LIKED_AT`
```python
# Add to favourites
waifu.insert_favourite(image="https://cdn.waifu.im/some_image.jpg")

# Remove from favourites
waifu.delete_favourite(image="https://cdn.waifu.im/some_image.jpg")

# Toggle
waifu.toggle_favourite(image="https://cdn.waifu.im/some_image.jpg")
```

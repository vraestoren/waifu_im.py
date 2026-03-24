from requests import Session

class WaifuIm:
    def __init__(self) -> None:
        self.api = "https://api.waifu.im"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        self.token = None

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def _get_status(self, endpoint: str, params: dict = None) -> int:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).status_code

    def _post_status(self, endpoint: str, params: dict = None) -> int:
        return self.session.post(
            f"{self.api}{endpoint}", params=params).status_code

    def _delete_status(self, endpoint: str, params: dict = None) -> int:
        return self.session.delete(
            f"{self.api}{endpoint}", params=params).status_code

    def _filter(self, data: dict) -> dict:
        return {k: v for k, v in data.items() if v is not None}

    def login_with_token(self, token: str) -> str:
        self.token = token
        self.session.headers["Authorization"] = f"Bearer {self.token}"
        return self.token

    def get_tags_list(self, full: bool = False) -> dict:
        return self._get(f"/tags?full={full}")

    def get_random_image(
            self,
            selected_tags: str = None,
            excluded_tags: str = None,
            is_nsfw: bool = False,
            is_gif: bool = False,
            orientation: str = "LANDSCAPE",
            is_many: bool = False) -> dict:
        params = self._filter({
            "selected_tags": selected_tags,
            "excluded_tags": excluded_tags,
            "gif": is_gif,
            "orientation": orientation,
            "many": is_many
        })
        return self._get(f"/random?is_nsfw={is_nsfw}", params)

    def report_image(
            self,
            image: str,
            description: str,
            user_id: int = None) -> int:
        params = self._filter({"user_id": user_id})
        return self._get_status(
            f"/report?image={image}&description={description}", params)

    def get_favourites(
            self,
            user_id: int = None,
            selected_tags: str = None,
            excluded_tags: str = None,
            is_nsfw: bool = False,
            is_gif: bool = False,
            order_by: str = "FAVOURITES",
            orientation: str = "LANDSCAPE",
            is_many: bool = False) -> dict:
        params = self._filter({
            "user_id": user_id,
            "selected_tags": selected_tags,
            "excluded_tags": excluded_tags,
            "gif": is_gif,
            "order_by": order_by,
            "orientation": orientation,
            "many": is_many
        })
        return self._get(f"/fav?is_nsfw={is_nsfw}", params)

    def insert_favourite(
            self, image: str, user_id: str = None) -> int:
        params = self._filter({"user_id": user_id})
        return self._post_status(f"/fav/insert?image={image}", params)

    def delete_favourite(
            self, image: str, user_id: str = None) -> int:
        params = self._filter({"user_id": user_id})
        return self._delete_status(f"/fav/delete?image={image}", params)

    def toggle_favourite(
            self, image: str, user_id: str = None) -> int:
        params = self._filter({"user_id": user_id})
        return self._post_status(f"/fav/toggle?image={image}", params)

    def get_image_info(self, image: str) -> dict:
        return self._get(f"/info?image={image}")

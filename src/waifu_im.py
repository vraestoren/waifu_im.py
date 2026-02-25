from requests import Session
	
class WaifuIm:
	def __init__(self) -> None:
		self.api = "https://api.waifu.im"
		self.public_api = "https://waifu.im"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
			"Content-Type": "application/json",
			"Connection": "keep-alive"
		}
		self.token = None

	def login_with_token(self, token: str) -> str:
		self.token = token
		self.session.headers["Authorization"] = f"Bearer {self.token}"
		return self.token

	def get_tags_list(self, full: bool = False) -> dict:
		return self.session.get(f"{self.api}/tags?full={full}").json()

	def get_random_image(
			self,
			selected_tags: str = None,
			excluded_tags: str = None,
			is_nsfw: bool = False,
			is_gif: bool = False,
			orientation: str = "LANDSCAPE",
			is_many: bool = False) -> dict:
		params = {
			"selected_tags": selected_tags,
			"excluded_tags": excluded_tags,
			"gif": is_gif,
			"orientation": orientation,
			"many": is_many
		}
		filtered_params = {
			key: value for key, value in params.items() if value is not None
		}
		return self.session.get(
			f"{self.api}/random?is_nsfw={is_nsfw}", params=filtered_params).json()

	def report_image(
			self,
			image: str,
			description: str,
			user_id: int = None) -> int:
		params = {"user_id": user_id} if user_id else {}
		return self.session.get(
			f"{self.api}/report?image={image}&description={description}", params=params).status_code

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
		params = {
			"user_id": user_id,
			"selected_tags": selected_tags,
			"excluded_tags": excluded_tags,
			"gif": is_gif,
			"order_by": order_by,
			"orientation": orientation,
			"many": is_many
		}
		filtered_params = {
			key: value for key, value in params.items() if value is not None
		}
		return self.session.get(
			f"{self.api}/fav?is_nsfw={is_nsfw}", params=filtered_params).json()

	def insert_favourite(
			self,
			image: str,
			user_id: str = None) -> int:
		params = {"user_id": user_id} if user_id else {}
		return self.session.post(
			f"{self.api}/fav/insert?image={image}", params=params).status_code

	def delete_favourite(
			self,
			image: str,
			user_id: str = None) -> int:
		params = {"user_id": user_id} if user_id else {}
		return self.session.delete(
			f"{self.api}/fav/delete?image={image}", params=params).status_code

	def toggle_favourite(
			self,
			image: str,
			user_id: str = None) -> int:
		params = {"user_id": user_id} if user_id else {}
		return self.session.post(
			f"{self.api}/fav/toggle?image={image}", params=params).status_code

	def get_image_info(self, image: str) -> dict:
		return self.session.get(
			f"{self.api}/info?image={image}").json()

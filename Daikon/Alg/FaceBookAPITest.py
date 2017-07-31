# -*- coding: utf-8 -*-
import facebook


token = "EAAKlWT7g6lYBABhikaFShLZC1SeAmEcvCZBSYQK2zFQrtMcU4gPrb8eJ62gHXYqCdr3aUoWYT9XfnYFEzgqSfK5IqHurZCR3ZBHZCsZAZBRrHKaIZA3ZBPAedfXMyYK3ZAnETfQ7djZCdLZAgK3hVivLNfyh3nlX4EkdJ69rlIySZArKviQVqFeXUFXFu"

graph = facebook.GraphAPI(access_token=token, version='2.9')

user = graph.get_object("me")

friends = graph.get_connections(10206974827803844, "friends")
print friends

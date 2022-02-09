# this script prepares web chat
# TODO: move webchat into a separate repo (subrepo) and build it with webpack
# then upload the built chat into web server
import os
import shutil

web_chat_source_dir = "./web_chat"
avatar_file="./personal_data/avatar/animated.gif"
web_chat_dist_dir = "./dist"

if os.path.exists(web_chat_dist_dir):
  shutil.rmtree(web_chat_dist_dir)

shutil.copytree(web_chat_source_dir, web_chat_dist_dir)
shutil.copyfile(avatar_file, web_chat_dist_dir + "/avatar.gif")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2020/8/14 12:39
# Author  : libin（libin09@netease.com）
# File    : config.py
# software: PyCharm
# time: 2020/8/14 12:39

import os
import time

BASE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(BASE_DIR)
DAY = time.strftime('%Y-%m-%d', time.localtime(time.time()))

ksong_package = "com.netease.karaoke"
ksong_package_debug = "com.netease.karaoke.debug"

music_package = "com.netease.cloudmusic"
music_package_debug = "com.netease.cloudmusic.debug"

MAINACTIVITY = "com.netease.cloudmusic.module.login.LoginActivity"

#车载的包名
music_car_package="com.netease.cloudmusic.hwcar"
music_car_MAINACTIVITY="com.netease.cloudmusic.home.MainActivity"

# TODO：指定待测试的正式包地址
PACKAGE = music_car_package

# TODO：指定待测试的debug包地址
PACKAGE_DEBUG = music_package_debug

"""
以下为云音乐的路由地址
例如：adb shell am start -a android.intent.action.VIEW -d 'orpheus://nm/account/about'
*云音乐用：orpheus
#跳转我的页面:minePage="orpheus://nm/main/mine"
"""
# 跳转播放页
songPlay = "song/1312166262"
# 跳转专辑详情
albumDetail = "album/83848829"
# 跳转歌单详情
playlistDetail = "playlist/2919023249"
# 跳转每日推荐
dailyRcmd = "songrcmd"
# 跳转艺人页详情
artist = "artist/12138269"
# 跳转个人主页
userDetail = "user/1300001885"
# 跳转云村广场
feedSquare = "nm/MLog/feedSquare"
# 跳转搜索页面
search_ksong = "search"
# 跳转动态详情页
eventDetail = "event?id={}&userId={}"
# 跳转设置页面
accountSetting = "settings"
# 设置页
setting = "settings/main"
# 跳转我的页面
minePage = "nm/main/mine"
# 跳转发现页面
discovery = "discovery/recommend"
# 跳转私人FM页面
private_FM = "privatefm"
# 扫一扫跳转页面
scan = "nm/base/scan"
# Mlog视频发布跳转
videoPublish = "nm/mlog/videoPublish"
# 在线播放音质选择页面
playQuality = "nm/setting/playQuality"
# 帐号页中的关于页面
about = "nm/account/about"
# 跳转至关注流
friendEvent = "nm/friends/event"
# 跳转至播客-推荐页（声音首页）
voice = "nm/main/voice"
# 跳转至个人发布的Mlog聚合页
personalMlog = "nm/mlog/personal?userId={}&title=%E4%BA%91%E9%9F%B3%E4%B9%90%E5%AE%A2%E6%9C%8D%E7%9A%84mlog"
# 我的资料页
myProfileModify = "settings/profilemodify"
# 跳转至鲸云音效页
jingyunEffect = "effect"
# 跳转至排行榜页
songRank = "discovery/songrank"
# 跳转至歌手榜页
artistList = "nm/toplist/artist?areaCode={}"
# 跳转至MV排行榜页
mvList = "nm/toplist/mv"
# 跳转至播单详情页
voiceList = "nm/voicelist/detail?id={}"

"""
以下为音街的路由地址
例如：adb shell am start -a android.intent.action.VIEW -d 'euterpe://nk/discover'
*音街用：euterpe
*云音乐用：orpheus
"""
# 发现-路由地址
discover = "nk/discover"
# 发现-关注tab路由地址
discoverFollow = "nk/discover/follow"
# 发现-推荐tab路由地址
discoverRecommend = "nk/discover/recommend"

# 录制独唱-音频
recordMainAudio = "nk/record/main?accompanyId={}"

# 录制合唱-音频
recordMainAudioWithOpusId = "nk/record/main?accompanyId={}&opusId={}"

# 录制独唱-视频
recordMainVideo = "nk/record/main?accompanyId={}&recordType=1"

# 录制合唱-视频
recordMainVideoWithOpusId = "nk/record/main?accompanyId={}&recordType=1&opusId={}"

# 点歌台
ktv = "nk/ktv"
# 点歌台-热门
ktvHot = "nk/ktv/hot"
# 点歌台-已点
ktvMine = "nk/ktv/mine"
# 点歌台-排行榜
ktvRank = "nk/ktv/rank"
# 点歌台-推荐
ktvRecommend = "nk/ktv/recommend"

# 我的-首页
me = "nk/me"
# 我的-合唱
meChorus = "nk/me/chorus"
# 我的-作品
meOpus = "nk/me/opus"
# 我的-喜欢
meLike = "nk/me/like"
# 我的-相册
userAlbumMine = "nk/user/album"

# 消息
message = "nk/message"
# 消息-评论
msssageComment = "nk/message/comment"
# 消息-消息详情页
messageDetail = "nk/message/detail?accid={}&sessionType={}"
# 消息-获赞
messageLike = "nk/message/like"
# 消息-私信
messagePrivate = "nk/message/private"
# 消息-访客
messageVisitor = "nk/message/visitor"

# 心情圈子页
moodDiaryCircle = "nk/moodDiary/circle?moodId={}&showType={}"
# 心情日记歌曲选择页
moodDiaryMain = "nk/moodDiary/main"

# 作品详情页(只传opusId)
opusDetail = "nk/opus/detail?opusId="

# 伴奏详情页(只传accompanyId)
accompanimentDetail = "nk/accompaniment/detail?accompanyId={}"

# 搜索
search_Ksong = "nk/search/entry"

# 设置-首页
settingMain = "nk/settings/main"
# 设置-关于页
settingsAbout = "nk/settings/about"
# 设置-账号管理
settingsAccount = "nk/settings/account"
# 设置-通用
settinsGeneral = "nk/settings/general"
# 设置-隐私设置
settingsPrivacy = "nk/settings/privacy"
# 设置-资料编辑
settingProfile = "nk/settings/profile"

# 话题详情页
topicDetail = "nk/topic/detail?id={}"

# 进入用户(艺人)-伴奏tab
accompArtistUser = "nk/user/accomp?userId={}&artistId={}"
# 进入用户-相册
userAlbum = "nk/user/album?userId={}"
# 进入用户-合唱tab
userChorus = "nk/user/chorus?userId={}"
# 进入用户-关注列表
userFollowee = "nk/user/followee?userId={}"
# 进入用户-主页(用户ID)
userHome = "nk/user/home?userId={}"
# 进入用户-喜欢tab
userLike = "nk/user/likes?userId={}"
# 进入用户-作品tab
userOpus = "nk/user/opus?userId={}"
# 进入用户-为你推荐tab
userSecr = "nk/user/secr?userId=6D4DE96785F3B6D5B63A402A109F1EAC"

# APP内打开H5页面
openUrl = "navigator.openURL?url='https://st.k.163.com/silence'"

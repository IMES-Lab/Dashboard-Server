from Helper.RestHelper import EdgeXRestHelper
from Helper.RestHelper.item import EdgeXRestItem

VIDEO_SERVICE_PREFIX = 'video service for '
VIDEO_PROFILE_PREFIX = 'video profile for '
VIDEO_INFO_PREFIX = 'video info for '

def initEdgeXWithVideoInformations(videos, videos_types, videos_models, edgex_host='http://localhost:48081/api/v1/'):
    videoInfo_restHelper = EdgeXRestHelper.VideoInfoRestHelper(API_HOST=edgex_host)

    # POST Addressable
    for idx in range(0, len(videos)):
        videoItem_addressable = EdgeXRestItem.Addressable(origin=1000000000000,
                                                          name=videos[idx])
        videoInfo_restHelper.post_addressable(videoItem_addressable)

    # POST Device Service
    for idx in range(0, len(videos)):
        videoItem_deviceService = EdgeXRestItem.DeviceService(origin=1000000000000,
                                                              name=VIDEO_SERVICE_PREFIX + videos[idx],
                                                              description='video service for video named ' + videos[
                                                                  idx],
                                                              labels=['vr', 'video', 'fov', 'service'],
                                                              addressable={'name': videos[idx]})
        videoInfo_restHelper.post_deviceService(videoItem_deviceService)

    # POST Device Profile
    for idx in range(0, len(videos)):
        videoItem_deviceProfile = EdgeXRestItem.DeviceProfile(origin=1000000000000,
                                                              name=VIDEO_PROFILE_PREFIX + videos[idx],
                                                              description='video profile for video named ' + videos[
                                                                  idx],
                                                              labels=['vr', 'video', 'fov', 'profile'],
                                                              commands=[],
                                                              manufacturer=videos_types[idx],
                                                              model=videos_models[idx])
        videoInfo_restHelper.post_deviceProfile(videoItem_deviceProfile)

    # POST Device Information
    for idx in range(0, len(videos)):
        videoItem_deviceInfo = EdgeXRestItem.DeviceInfo(origin=1000000000000,
                                                        name=VIDEO_INFO_PREFIX + videos[idx],
                                                        description='video information for video named ' + videos[idx],
                                                        labels=['vr', 'video', 'fov', 'info'],
                                                        addressable={'name': videos[idx]},
                                                        adminState='UNLOCKED',
                                                        operatingState='ENABLED',
                                                        service={'name': VIDEO_SERVICE_PREFIX + videos[idx]},
                                                        profile={'name': VIDEO_PROFILE_PREFIX + videos[idx]})
        videoInfo_restHelper.post_deviceInfo(videoItem_deviceInfo)

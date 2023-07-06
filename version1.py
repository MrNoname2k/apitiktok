from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent,FollowEvent,GiftEvent,MicBattleStartEvent,MicBattleUpdateEvent,RankingUpdateEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@meowwdayy")
commentTimes = 0
listGift = []


  
# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):

    print("Connected to Room ID:", client.room_id)


@client.on("ranking_update")
async def on_connect(event: RankingUpdateEvent):
    print(f"{event.user.unique_id} has the rank #{event.rank} for the {event.type} leaderboard.")



# Notice no decorator?
async def on_comment(event: CommentEvent):
    global commentTimes 
    commentTimes += 1
    print(f"{event.user.nickname} -> {event.comment} -> Tổng comment : {commentTimes}")


# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"@{event.user.unique_id} Đã thích phiên live ! ")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"@{event.user.unique_id} Đã theo dõi !")

@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        coin = event.gift.count * event.gift.info.diamond_count
        print(f"{event.user.unique_id} sent {event.gift.count}x \"{event.gift.info.name}\"-Coin: {coin}")

    # Non-streakable gift
    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent \"{event.gift.info.name}\" - Coin : {event.gift.info.diamond_count}")


@client.on("mic_battle_start")
async def on_connect(event: MicBattleStartEvent):
    print(f" Mic PK bắt đầu !")

@client.on("mic_battle_update")
async def on_connect(event: MicBattleUpdateEvent):
    print(f"An army in the mic battle has received points, or the status of the battle has changed!")

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
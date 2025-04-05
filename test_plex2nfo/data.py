HTTP_DATA = {
    "/": """<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="26" allowCameraUpload="1" allowChannelAccess="1" allowMediaDeletion="1" allowSharing="1" allowSync="1" allowTuners="1" apiVersion="0.2.0" backgroundProcessing="1" certificate="1" companionProxy="1" countryCode="fra" diagnostics="logs,databases,streaminglogs" eventStream="1" friendlyName="maison" hubSearch="1" itemClusters="1" livetv="7" machineIdentifier="adfb6ec5473244904db960d8c698394f442327b1" mediaProviders="1" multiuser="1" musicAnalysis="2" myPlex="1" myPlexMappingState="mapped" myPlexSigninState="ok" myPlexSubscription="0" myPlexUsername="plex@19pouces.net" offlineTranscode="1" ownerFeatures="00077925-6031-401b-8679-f6617ed0cec6,007fb90d-2224-4d24-bd42-e87ffde13558,044a1fac-6b55-47d0-9933-25a035709432,04d7d794-b76c-49ef-9184-52f8f1f501ee,05826f20-284b-4bcb-b45c-2367e5c0ea72,06d14b9e-2af8-4c2b-a4a1-ea9d5c515824,0e2acda2-d70d-4df6-96e0-f63cf264d217,0eee866d-782b-4dfd-b42b-3bbe8eb0af16,1417df52-986e-4e4b-8dcd-3997fbc5c976,1b870b8e-f1a7-497c-80b2-857d45f3123f,1f952ea5-0837-44cb-8539-a69a14a75d4a,228a6439-ee2f-4a9b-b0fc-1bfcd48b5095,22b27e12-472e-4383-92ea-2ec3976d8e72,24b4cf36-b296-4002-86b7-f1adb657e76a,2797e341-b062-46ed-862f-0acbba5dd522,298a11d3-9324-4104-8047-0ac10df4a8a6,2ea0e464-ea4f-4be2-97c1-ce6ed4b377dd,300231e0-69aa-4dce-97f4-52d8c00e3e8c,34ddfac9-3a76-459a-974d-591520b809dd,34e182bd-2f62-4678-a9e9-d13b3e25019d,39dbdd84-8339-4736-96a1-0eb105cc2e08,3ae06d3a-a76b-435e-8cef-2d2008610ba2,3c376154-d47e-4bbf-9428-2ea2592fd20a,3eb2789b-200c-4a15-91d2-dedfe560953c,3f6baa76-7488-479a-9e4f-49ff2c0d3711,4742780c-af9d-4b44-bf5b-7b27e3369aa8,4b522f91-ae89-4f62-af9c-76f44d8ef61c,4cd4dc0e-6cbe-456c-9988-9f073fadcd73,52ee04dc-2b82-4142-9e0a-e7ce8087c5b6,547514ab-3284-46e5-af77-bbaff247e3fc,567033ef-ffee-44fb-8f90-f678077445f9,5b6190a9-77a4-477e-9fbc-c8118e35a4c1,5d819d02-5d04-4116-8eec-f49def4e2d6f,5e2a89ec-fb26-4234-b66e-14d37f35dff2,62b1e357-5450-41d8-9b60-c7705f750849,644c4466-05fa-45e0-a478-c594cf81778f,64adaa4e-aa7e-457d-b385-51438216d7fe,65685ff8-4375-4e4c-a806-ec1f0b4a8b7f,67c80530-eae3-4500-a9fa-9b6947d0f6d1,68747f3a-ce13-46ce-9274-1e0544c9f500,6b85840c-d79d-40c2-8d8f-dfc0b7d26776,6c4d66d9-729d-49dc-b70d-ab2652abf15a,6d7be725-9a96-42c7-8af4-01e735138822,7b392594-6949-4736-9894-e57a9dfe4037,7f46bf17-fabf-4f96-99a2-cf374f6eed71,81c8d5fa-8d90-4833-aa10-a31a51310e2f,849433b0-ef60-4a71-9dd9-939bc01f5362,8536058d-e1dd-4ae7-b30f-e8b059b7cc17,85ebfb7b-77fb-4afd-bb1a-2fe2fefdddbe,86da2200-58db-4d78-ba46-f146ba25906b,88aba3a3-bd62-42a5-91bb-0558a4c1db57,8b46de05-1f96-4278-87b3-010ba5b1e386,96cac76e-c5bc-4596-87eb-4fdfef9aaa11,9a67bff2-cb80-4bf9-81c6-9ad2f4c78afd,9aea4ca5-2095-4619-9339-88c1e662fde6,9e93f8a8-7ccd-4d15-99fa-76a158027660,a19d495a-1cef-4f7c-ab77-5186e63e17f7,a3d2d5c4-46a0-436e-a2d6-80d26f32b369,a536a6e1-0ece-498a-bf64-99b53c27de3a,a548af72-b804-4d05-8569-52785952d31d,a6f3f9b3-c10c-4b94-ad59-755e30ac6c90,abd37b14-706c-461f-8255-fa9563882af3,adaptive_bitrate,af291e9e-813f-4467-8779-5d215abc3b5f,b227c158-e062-4ff1-95d8-8ed11cecafb1,b2403ac6-4885-4971-8b96-59353fd87c72,b25b878c-4f60-4337-9f6b-2d97ef41d036,b3b87f19-5ccd-4b14-bb62-b9d7b982392e,b46d16ae-cbd6-4226-8ee9-ab2b27e5dd42,b5874ecb-6610-47b2-8906-1b5a897acb02,b612f571-83c3-431a-88eb-3f05ce08da4a,b77e6744-c18d-415a-8e7c-7aac5d7a7750,bb50c92f-b412-44fe-8d8a-b1684f212a44,bec2ba97-4b25-472b-9cfc-674f5c68c2ae,c36a6985-eee3-4400-a394-c5787fad15b5,c55d5900-b546-416d-a8c5-45b24a13e9bc,c7ae6f8f-05e6-48bb-9024-c05c1dc3c43e,c987122a-a796-432f-af00-953821c127bb,c9d9b7ee-fdd9-474e-b143-5039c04e9b9b,camera_upload,cb151c05-1943-408a-b37c-06f7d409d6bb,cc9bea3b-11ab-4402-a222-4958bb129cab,ccef9d3a-537a-43d9-8161-4c7113c6e2bb,ce8f644e-87ce-4ba5-b165-fadd69778019,collections,d14556be-ae6d-4407-89d0-b83953f4789a,d1477307-4dac-4e57-9258-252e5b908693,d20f9af2-fdb1-4927-99eb-a2eb8fbff799,d29f0ee0-3d3a-46c3-b582-4bc69bc17c29,d85cb60c-0986-4a02-b1e1-36c64c609712,d9f42aea-bc9d-47db-9814-cd7a577aff48,dab501df-5d99-48ef-afc2-3e839e4ddc9a,db965785-ca5c-46fd-bab6-7b3d29c18492,de65add8-2782-4bb8-b156-e0b57a844479,download_certificates,e45bc5ae-1c3a-4729-922b-c69388c571b7,e4a9fd6f-4105-476b-bc57-adccd009323b,e5fe743c-af51-468a-b7e2-aabf0e79030c,e66aa31c-abdd-483d-93bc-e17485d8837f,e703655b-ee05-4e24-97e3-a138da62c425,ea442c16-044a-4fa7-8461-62643f313c62,ea791163-c28d-4b7c-af88-bcc9553b206d,ee352392-2934-4061-ba35-5f3189f19ab4,f1ac7a53-c524-4311-9a27-713562fc24fa,f3235e61-c0eb-4718-ac0a-7d6eb3d8ff75,f3a99481-9671-4274-a0d3-4c06a72ef746,f83450e2-759a-4de4-8b31-e4a163896d43,f8463032-28f1-447b-a76c-8b57a071acad,f87f382b-4a41-4951-b4e4-d5822c69e4c6,f8ea4f37-c554-476a-8852-1cbd2912f3f6,fb34e64d-cd89-47b8-8bae-a6d20c542bae,fec722a0-a6d4-4fbd-96dc-4ffb02b072c5,federated-auth,home,kevin-bacon,livetv,loudness,radio,server-manager,shared-radio,tuner-sharing,type-first,unsupportedtuners" platform="Linux" platformVersion="6.8.0-55-generic" pluginHost="1" pushNotifications="0" readOnlyLibraries="0" streamingBrainABRVersion="3" streamingBrainVersion="2" sync="1" transcoderActiveVideoSessions="0" transcoderAudio="1" transcoderLyrics="1" transcoderPhoto="1" transcoderSubtitles="1" transcoderVideo="1" transcoderVideoBitrates="64,96,208,320,720,1500,2000,3000,4000,8000,10000,12000,20000" transcoderVideoQualities="0,1,2,3,4,5,6,7,8,9,10,11,12" transcoderVideoResolutions="128,128,160,240,320,480,768,720,720,1080,1080,1080,1080" updatedAt="1743847598" updater="1" version="1.41.5.9522-a96edc606" voiceSearch="1">
<Directory count="1" key="actions" title="actions" />
<Directory count="1" key="activities" title="activities" />
<Directory count="1" key="butler" title="butler" />
<Directory count="1" key="channels" title="channels" />
<Directory count="1" key="clients" title="clients" />
<Directory count="1" key="devices" title="devices" />
<Directory count="1" key="diagnostics" title="diagnostics" />
<Directory count="1" key="downloadQueue" title="downloadQueue" />
<Directory count="1" key="hubs" title="hubs" />
<Directory count="3" key="library" title="library" />
<Directory count="3" key="livetv" title="livetv" />
<Directory count="3" key="media" title="media" />
<Directory count="1" key="neighborhood" title="neighborhood" />
<Directory count="1" key="playQueues" title="playQueues" />
<Directory count="1" key="playlists" title="playlists" />
<Directory count="1" key="resources" title="resources" />
<Directory count="1" key="search" title="search" />
<Directory count="1" key="server" title="server" />
<Directory count="1" key="servers" title="servers" />
<Directory count="1" key="service" title="service" />
<Directory count="1" key="statistics" title="statistics" />
<Directory count="1" key="system" title="system" />
<Directory count="1" key="transcode" title="transcode" />
<Directory count="1" key="updater" title="updater" />
<Directory count="1" key="user" title="user" />
<Directory count="1" key="video" title="video" />
</MediaContainer>""",
    "/library": """<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="3" allowSync="0" art="/:/resources/library-art.png" content="" identifier="com.plexapp.plugins.library" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1740148659" title1="Plex Library" title2="">
<Directory key="sections" title="Library Sections" />
<Directory key="recentlyAdded" title="Recently Added Content" />
<Directory key="onDeck" title="On Deck Content" />
</MediaContainer>
""",
    "/library/sections": """<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="13" allowSync="0" title1="Plex Library">
<Directory allowSync="1" art="/:/resources/movie-fanart.jpg" composite="/library/sections/32/composite/1743847598" filters="1" refreshing="0" thumb="/:/resources/movie.png" key="32" type="movie" title="Tests" agent="tv.plex.agents.movie" scanner="Plex Movie" language="fr-FR" uuid="d3c0f683-7cfb-40ab-8dc3-4ec70fc4cc95" updatedAt="1743847598" createdAt="1743847561" scannedAt="1743847598" content="1" directory="1" contentChangedAt="7104227" hidden="2">
<Location id="61" path="/data/Films-Test" />
</Directory>
</MediaContainer>
""",
    "/library/sections/32/all": """<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" totalSize="1" offset="0" allowSync="1" art="/:/resources/movie-fanart.jpg" content="secondary" identifier="com.plexapp.plugins.library" librarySectionID="32" librarySectionTitle="Tests" librarySectionUUID="d3c0f683-7cfb-40ab-8dc3-4ec70fc4cc95" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1740148659" thumb="/:/resources/movie.png" title1="Tests" title2="All Tests" viewGroup="movie">
<Video ratingKey="73564" key="/library/metadata/73564" guid="plex://movie/5d776f37fb0d55001f5da6b5" slug="the-kings-man" studio="Marv" type="movie" title="The King&#39;s Man : Premi&#232;re Mission" titleSort="King&#39;s Man : Premiere Mission" originalTitle="The King&#39;s Man" contentRating="R" summary="En 1902, l&#39;aristocrate Orlando, duc d&#39;Oxford, perd sa femme Emily lors d&#39;une mission humanitaire en Afrique du Sud lors de la seconde guerre des Boers ; leur jeune fils Conrad assiste lui aussi &#224; sa mort. Douze ans plus tard, le pacifiste convaincu Orlando sent qu&#39;un conflit mondial menace. Il tente par ailleurs de dissuader son fils, &#226;g&#233; de 18 ans, de s&#39;engager dans l&#39;arm&#233;e britannique. Il a implor&#233; son grand ami, le secr&#233;taire d&#39;&#201;tat &#224; la Guerre Horatio Herbert Kitchener, de bloquer sa demande d&#39;incorporation. Aid&#233; par ses domestiques Shola et Polly, le duc a par ailleurs cr&#233;&#233; un r&#233;seau d&#39;espionnage mondial et se renseigne sur la menace qui plane sur l&#39;Europe. En effet, dans l&#39;ombre, une myst&#233;rieuse organisation souhaite renverser l&#39;ordre mondial." rating="4.1" audienceRating="8.0" viewCount="1" lastViewedAt="1645737306" year="2021" tagline="D&#233;couvrez les origines de la toute premi&#232;re agence de renseignement ind&#233;pendante." thumb="/library/metadata/73564/thumb/1743847562" art="/library/metadata/73564/art/1743847562" duration="7837728" originallyAvailableAt="2021-12-22" addedAt="1743847517" updatedAt="1743847562" audienceRatingImage="rottentomatoes://image.rating.upright" hasPremiumExtras="1" hasPremiumPrimaryExtra="1" ratingImage="rottentomatoes://image.rating.rotten">
<Media id="72807" duration="7837728" bitrate="3540" width="1920" height="800" aspectRatio="2.35" audioChannels="6" audioCodec="eac3" videoCodec="hevc" videoResolution="1080" container="mkv" videoFrameRate="24p" videoProfile="main 10">
<Part id="108911" key="/library/parts/108911/1743847517/file.mkv" duration="7837728" file="/data/Films-Test/The King&#39;s Man - Premie&#768;re Mission (2021)/The King&#39;s Man - Premie&#768;re Mission (2021).mkv" size="3467857242" container="mkv" videoProfile="main 10" />
</Media>
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="coverPoster" url="/library/metadata/73564/thumb/1743847562" />
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="background" url="/library/metadata/73564/art/1743847562" />
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="clearLogo" url="/library/metadata/73564/clearLogo/1743847562" />
<UltraBlurColors topLeft="442603" topRight="286778" bottomRight="8c4a08" bottomLeft="6c400c" />
<Guid id="imdb://tt6856242" />
<Guid id="tmdb://476669" />
<Guid id="tvdb://9846" />
<Genre tag="Action" />
<Genre tag="Adventure" />
<Country tag="United Kingdom" />
<Country tag="United States of America" />
<Director tag="Matthew Vaughn" />
<Writer tag="Matthew Vaughn" />
<Writer tag="Karl Gajdusek" />
<Role tag="Ralph Fiennes" />
<Role tag="Gemma Arterton" />
<Role tag="Rhys Ifans" />
</Video>
</MediaContainer>
""",
    "/library/metadata/73564": """<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" allowSync="1" identifier="com.plexapp.plugins.library" librarySectionID="32" librarySectionTitle="Tests" librarySectionUUID="d3c0f683-7cfb-40ab-8dc3-4ec70fc4cc95" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1740148659">
<Video ratingKey="73564" key="/library/metadata/73564" guid="plex://movie/5d776f37fb0d55001f5da6b5" slug="the-kings-man" studio="Marv" type="movie" title="The King&#39;s Man : Premi&#232;re Mission" titleSort="King&#39;s Man : Premiere Mission" librarySectionTitle="Tests" librarySectionID="32" librarySectionKey="/library/sections/32" originalTitle="The King&#39;s Man" contentRating="R" summary="En 1902, l&#39;aristocrate Orlando, duc d&#39;Oxford, perd sa femme Emily lors d&#39;une mission humanitaire en Afrique du Sud lors de la seconde guerre des Boers ; leur jeune fils Conrad assiste lui aussi &#224; sa mort. Douze ans plus tard, le pacifiste convaincu Orlando sent qu&#39;un conflit mondial menace. Il tente par ailleurs de dissuader son fils, &#226;g&#233; de 18 ans, de s&#39;engager dans l&#39;arm&#233;e britannique. Il a implor&#233; son grand ami, le secr&#233;taire d&#39;&#201;tat &#224; la Guerre Horatio Herbert Kitchener, de bloquer sa demande d&#39;incorporation. Aid&#233; par ses domestiques Shola et Polly, le duc a par ailleurs cr&#233;&#233; un r&#233;seau d&#39;espionnage mondial et se renseigne sur la menace qui plane sur l&#39;Europe. En effet, dans l&#39;ombre, une myst&#233;rieuse organisation souhaite renverser l&#39;ordre mondial." rating="4.1" audienceRating="8.0" viewCount="1" lastViewedAt="1645737306" thumbBlurHash="TEBfb0a~jEt7WYS30fWAIpfmjYM}" artBlurHash="LqQm3O_4xu9F%2R*WBt7-=IURjxt" year="2021" tagline="D&#233;couvrez les origines de la toute premi&#232;re agence de renseignement ind&#233;pendante." thumb="/library/metadata/73564/thumb/1743847562" art="/library/metadata/73564/art/1743847562" duration="7837728" originallyAvailableAt="2021-12-22" addedAt="1743847517" updatedAt="1743847562" audienceRatingImage="rottentomatoes://image.rating.upright" hasPremiumExtras="1" hasPremiumPrimaryExtra="1" ratingImage="rottentomatoes://image.rating.rotten">
<Media id="72807" duration="7837728" bitrate="3540" width="1920" height="800" aspectRatio="2.35" audioChannels="6" audioCodec="eac3" videoCodec="hevc" videoResolution="1080" container="mkv" videoFrameRate="24p" videoProfile="main 10">
<Part id="108911" key="/library/parts/108911/1743847517/file.mkv" duration="7837728" file="/data/Films-Test/The King&#39;s Man - Premie&#768;re Mission (2021)/The King&#39;s Man - Premie&#768;re Mission (2021).mkv" size="3467857242" container="mkv" videoProfile="main 10">
<Stream id="272734" streamType="1" default="1" codec="hevc" index="0" bitrate="3540" bitDepth="10" chromaLocation="left" chromaSubsampling="4:2:0" codedHeight="800" codedWidth="1920" colorPrimaries="bt709" colorRange="tv" colorSpace="bt709" colorTrc="bt709" frameRate="23.810" height="800" level="120" profile="main 10" refFrames="1" width="1920" displayTitle="1080p" extendedDisplayTitle="1080p (HEVC Main 10)">
</Stream>
<Stream id="272735" streamType="2" selected="1" default="1" codec="eac3" index="1" channels="6" bitrate="256" language="French" languageTag="fr" languageCode="fra" audioChannelLayout="5.1(side)" samplingRate="48000" title="VFF" displayTitle="French (EAC3 5.1)" extendedDisplayTitle="VFF (French EAC3 5.1)">
</Stream>
<Stream id="272736" streamType="2" codec="eac3" index="2" channels="6" bitrate="768" language="English" languageTag="en" languageCode="eng" audioChannelLayout="5.1(side)" samplingRate="48000" title="VO" displayTitle="English (EAC3 5.1)" extendedDisplayTitle="VO (English EAC3 5.1)">
</Stream>
<Stream id="272737" streamType="3" selected="1" default="1" forced="1" codec="srt" index="3" language="French" languageTag="fr" languageCode="fra" title="Forced" displayTitle="French Forced" extendedDisplayTitle="Forced (French SRT)">
</Stream>
<Stream id="272738" streamType="3" codec="srt" index="4" bitrate="0" language="French" languageTag="fr" languageCode="fra" title="Full" displayTitle="French" extendedDisplayTitle="Full (French SRT)">
</Stream>
<Stream id="272739" streamType="3" codec="srt" index="5" bitrate="0" language="English" languageTag="en" languageCode="eng" title="Full" displayTitle="English" extendedDisplayTitle="Full (English SRT)">
</Stream>
</Part>
</Media>
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="coverPoster" url="/library/metadata/73564/thumb/1743847562" />
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="background" url="/library/metadata/73564/art/1743847562" />
<Image alt="The King&#39;s Man : Premi&#232;re Mission" type="clearLogo" url="/library/metadata/73564/clearLogo/1743847562" />
<UltraBlurColors topLeft="442603" topRight="286778" bottomRight="8c4a08" bottomLeft="6c400c" />
<Genre id="92" filter="genre=92" tag="Action" />
<Genre id="13795" filter="genre=13795" tag="Adventure" />
<Genre id="146" filter="genre=146" tag="Thriller" />
<Genre id="1487" filter="genre=1487" tag="Drame" />
<Genre id="4147" filter="genre=4147" tag="Histoire" />
<Country id="4682" filter="country=4682" tag="United Kingdom" />
<Country id="119038" filter="country=119038" tag="United States of America" />
<Guid id="imdb://tt6856242" />
<Guid id="tmdb://476669" />
<Guid id="tvdb://9846" />
<Rating image="imdb://image.rating" value="6.3" type="audience" />
<Rating image="rottentomatoes://image.rating.rotten" value="4.1" type="critic" />
<Rating image="rottentomatoes://image.rating.upright" value="8.0" type="audience" />
<Rating image="themoviedb://image.rating" value="6.8" type="audience" />
<Director id="190530" filter="director=190530" tag="Matthew Vaughn" tagKey="5d776826e6d55c002040af53" thumb="https://metadata-static.plex.tv/3/people/37809b0934d7ae73f85791903aa1dc9c.jpg" />
<Writer id="190531" filter="writer=190531" tag="Matthew Vaughn" tagKey="5d776826e6d55c002040af53" thumb="https://metadata-static.plex.tv/3/people/37809b0934d7ae73f85791903aa1dc9c.jpg" />
<Writer id="205615" filter="writer=205615" tag="Karl Gajdusek" tagKey="5d776855594b2b001e688d36" thumb="https://metadata-static.plex.tv/e/people/e0724dec3c9aa8846b88e2e64f6ec987.jpg" />
<Writer id="190532" filter="writer=190532" tag="Mark Millar" tagKey="5d7768ebad5437001f752ace" thumb="https://metadata-static.plex.tv/1/people/1fb7ab93ad4801c176b5b4928049cd15.jpg" />
<Writer id="265434" filter="writer=265434" tag="Dave Gibbons" tagKey="5d7768a8fb0d55001f516c4b" thumb="https://metadata-static.plex.tv/6/people/6858914d3c9a7f65b975acef716c580c.jpg" />
<Role id="162545" filter="actor=162545" tag="Ralph Fiennes" tagKey="5d7768267e9a3c0020c6a9eb" role="Orlando Oxford" thumb="https://metadata-static.plex.tv/c/people/cd1165b587e82edf3ddd42cb24fe3712.jpg" />
<Role id="184449" filter="actor=184449" tag="Gemma Arterton" tagKey="5d776833f59e5800218989c8" role="Polly" thumb="https://metadata-static.plex.tv/e/people/eacfd4f0cdb70109deefc89f681cee87.jpg" />
<Role id="165371" filter="actor=165371" tag="Rhys Ifans" tagKey="5d77682685719b001f3a0b2f" role="Grigori Rasputin" thumb="https://metadata-static.plex.tv/e/people/e559281a3680520f8dfc7a94051b6fa2.jpg" />
<Role id="165655" filter="actor=165655" tag="Matthew Goode" tagKey="5d776825eb5d26001f1dd0d3" role="Morton" thumb="https://metadata-static.plex.tv/f/people/f05e7838181ffa38bd5033c4612adf4c.jpg" />
<Role id="185476" filter="actor=185476" tag="Tom Hollander" tagKey="5d77682654c0f0001f301be1" role="King George / Kaiser Wilhelm / Tsar Nicholas" thumb="https://metadata-static.plex.tv/b/people/bc5976c2b1a7d8fbdbf8c6a05a681765.jpg" />
<Role id="265435" filter="actor=265435" tag="Harris Dickinson" tagKey="5d776c7ffb0d55001f5892ef" role="Conrad Oxford" thumb="https://metadata-static.plex.tv/1/people/120db49605768de991537a6100f500d5.jpg" />
<Role id="164356" filter="actor=164356" tag="Daniel Br&#252;hl" tagKey="5d776825a091de001f2e60cd" role="Erik Jan Hanussen" thumb="https://metadata-static.plex.tv/a/people/aec28e6e83c34fbea5159d5a15ed0813.jpg" />
<Role id="167841" filter="actor=167841" tag="Djimon Hounsou" tagKey="5d7768267228e5001f1dcdb9" role="Shola" thumb="https://metadata-static.plex.tv/8/people/8730541ac598153cc649a566c8045fbd.jpg" />
<Role id="165207" filter="actor=165207" tag="Charles Dance" tagKey="5d7768258718ba001e3118c3" role="Kitchener" thumb="https://metadata-static.plex.tv/7/people/7ae2abd1dca0c1aa8b5505cd6e00b19e.jpg" />
<Role id="197742" filter="actor=197742" tag="Shaun McKee" tagKey="5d776e5c594b2b001e7219ba" role="Camp Guard #1" thumb="https://metadata-static.plex.tv/people/5d776e5c594b2b001e7219ba.jpg" />
<Role id="292782" filter="actor=292782" tag="Peter York" tagKey="5ec423d0254ba70038dbeb50" role="Camp Guard #2" />
<Role id="174533" filter="actor=174533" tag="Alexandra Maria Lara" tagKey="5d77682685719b001f3a0b67" role="Emily Oxford" thumb="https://metadata-static.plex.tv/9/people/9532909e28dbfda6f0c067d7811c9701.jpg" />
<Role id="292759" filter="actor=292759" tag="Alexander Shaw" tagKey="5f3fdcfa86422500427cf831" role="Young Conrad" thumb="https://metadata-static.plex.tv/a/people/a7d8b20b5b1bb23b828eb5b05d965978.jpg" />
<Role id="292760" filter="actor=292760" tag="Bevan Viljoen" tagKey="5dd876618e9524001faf5a98" role="Boer Sniper" thumb="https://metadata-static.plex.tv/6/people/620c247e399d7a5fa9262be8f668b7af.jpg" />
<Role id="265444" filter="actor=265444" tag="Shaun Scott" tagKey="5d77697347dd6e001f6c5a70" role="Kingsman Tailor #1" thumb="https://metadata-static.plex.tv/b/people/be92444ea8afa0d99886a804753f2c7a.jpg" />
<Role id="190768" filter="actor=190768" tag="Andrew Bridgmont" tagKey="5d776a3996b655001fde74b3" role="Kingsman Tailor #2" thumb="https://metadata-static.plex.tv/people/5d776a3996b655001fde74b3.jpg" />
<Role id="265438" filter="actor=265438" tag="Olivier Richters" tagKey="5d77706281ba41001faeee29" role="Huge Machinery Shack Guard" thumb="https://metadata-static.plex.tv/2/people/2681dd9d35fdd523a6b48d0472012bfc.jpg" />
<Role id="265446" filter="actor=265446" tag="Valerie Pachner" tagKey="5d776b6efb0d55001f567d92" role="Mata Hari" thumb="https://metadata-static.plex.tv/3/people/393eb5422d9f45a69d86ade8c5aa437d.jpg" />
<Role id="185481" filter="actor=185481" tag="Joel Basman" tagKey="5d77688b47dd6e001f6bb66f" role="Gavrilo Princip" thumb="https://metadata-static.plex.tv/8/people/8053346b709f9d5357db7e84ea614bae.jpg" />
<Role id="174307" filter="actor=174307" tag="Todd Boyce" tagKey="5d7768243c3c2a001fbca937" role="Dupont" thumb="https://metadata-static.plex.tv/6/people/6f5cb572025da29c829b33060fe77155.jpg" />
<Role id="282758" filter="actor=282758" tag="Richard Stephenson Winter" tagKey="5f4035521ae710004107192b" role="Shepherd&#39;s Flock Member #2" />
<Role id="201617" filter="actor=201617" tag="Takako Akashi" tagKey="5d776afc7a53e9001e715e4a" role="Shepherd&#39;s Flock Member #3" thumb="https://metadata-static.plex.tv/5/people/5fa77edc42ac7055d8815b5d34175496.jpg" />
<Role id="212119" filter="actor=212119" tag="Thorston Manderlay" tagKey="5d7768345af944001f1f9b43" role="Shepherd&#39;s Flock Member #4" thumb="https://metadata-static.plex.tv/people/5d7768345af944001f1f9b43.jpg" />
<Role id="271686" filter="actor=271686" tag="Terence Anderson" tagKey="624713234502fd5d0c263764" role="Shepherd&#39;s Flock Member #5" />
<Role id="162572" filter="actor=162572" tag="Andy Cheung" tagKey="5d776a377a53e9001e6fdf0d" role="Shepherd&#39;s Flock Member #6" thumb="https://metadata-static.plex.tv/9/people/9f7caf2d6275dc1c76f324e26cf7ed45.jpg" />
<Role id="186672" filter="actor=186672" tag="Ron Cook" tagKey="5d776826999c64001ec2c3e6" role="Archduke Franz Ferdinand of Austria" thumb="https://metadata-static.plex.tv/people/5d776826999c64001ec2c3e6.jpg" />
<Role id="265447" filter="actor=265447" tag="Barbara Drennan" tagKey="5d7769e247dd6e001f6cbc14" role="Sophie, Duchess of Hohenberg" thumb="https://metadata-static.plex.tv/people/5d7769e247dd6e001f6cbc14.jpg" />
<Role id="265439" filter="actor=265439" tag="Maja Simonsen" tagKey="5f405d7c03883a0040bba063" role="Pretty Girl" thumb="https://metadata-static.plex.tv/b/people/b3c14e31a26d69f1001ae67b114bc096.jpg" />
<Role id="211536" filter="actor=211536" tag="Benedick Blythe" tagKey="5d776829f54112001f5bc25e" role="Saravejo General" thumb="https://image.tmdb.org/t/p/original/xNux5UAQDlrYTiBjPAu180Fai87.jpg" />
<Role id="292781" filter="actor=292781" tag="Max Count" tagKey="5f3fce1252f2000041496ef8" role="Young King George" />
<Role id="292780" filter="actor=292780" tag="Emil Oksanen" tagKey="5f3fcddbcc4920003b2b3639" role="Young Kaiser Wilhelm" />
<Role id="292779" filter="actor=292779" tag="George Gooderham" tagKey="5f3fceacfea1a1003f977e68" role="Young Tsar Nicholas" />
<Role id="271682" filter="actor=271682" tag="Alexa Povah" tagKey="5d776df9ad5437001f7e6988" role="Queen Victoria" thumb="https://metadata-static.plex.tv/f/people/fb37625afac3e387308e2e0debdb877f.jpg" />
<Role id="173703" filter="actor=173703" tag="Branka Kati&#263;" tagKey="5d7768293c3c2a001fbcb9a3" role="Tsarina Alix" thumb="https://metadata-static.plex.tv/b/people/bda90ba13185cb6db87501957bbbd700.jpg" />
<Role id="271681" filter="actor=271681" tag="Alexander Shefler" tagKey="624713232895c61a90b84270" role="Tsarevich Alexei" />
<Role id="292761" filter="actor=292761" tag="Rosie Goddard" tagKey="5d776b32f617c9002017334d" role="Grand Duchess Anastasia" thumb="https://metadata-static.plex.tv/f/people/f19888c8e4d9daeb9461958e96fb479f.jpg" />
<Role id="282751" filter="actor=282751" tag="Dora Davis" tagKey="5f3fc0562e2b260040a857eb" role="Grand Duchess Maria" thumb="https://metadata-static.plex.tv/4/people/436da65167187263b0fc7279b49ee9ee.jpg" />
<Role id="292778" filter="actor=292778" tag="Lucia Jade Barker" tagKey="60ebfd4bd8000e002daf1ed2" role="Grand Duchess Olga" />
<Role id="292777" filter="actor=292777" tag="Molly McGeachin" tagKey="5f3fc85503883a0040ab1861" role="Grand Duchess Tatiana" />
<Role id="271678" filter="actor=271678" tag="Angus Castle-Doughty" tagKey="5ec41eb843d47400431f81e0" role="British Soldier" thumb="https://metadata-static.plex.tv/f/people/f9e1f0abfa649aaa12d926ec947d97fb.jpg" />
<Role id="292776" filter="actor=292776" tag="Jed O&#39;Hagan" tagKey="5f4059675a76a80042dc9b4d" role="British Soldier #2" />
<Role id="292775" filter="actor=292775" tag="Thomas Mahy" tagKey="5f3fd80a02101b0040ee243c" role="British Soldier #3" />
<Role id="265441" filter="actor=265441" tag="Connor Calland" tagKey="5dfc18f1b308ca001e975765" role="British Soldier #4" thumb="https://metadata-static.plex.tv/e/people/edae396ff3f27383ad5c86651acd2cd1.jpg" />
<Role id="292774" filter="actor=292774" tag="James Musgrave" tagKey="5f3fec0d03883a0040ae71c6" role="Lieutenant" thumb="https://metadata-static.plex.tv/e/people/e94ef4a9c0ef47dca56a0249ac4b36e9.jpg" />
<Role id="265437" filter="actor=265437" tag="Martin Razpopov" tagKey="5e1656db316a39003efa2c80" role="Sarajevo Prison Warden" thumb="https://metadata-static.plex.tv/people/5e1656db316a39003efa2c80.jpg" />
<Role id="271674" filter="actor=271674" tag="Aaron Vodovoz" tagKey="5d776b9f9ab544002150d941" role="Felix Yusupov" thumb="https://metadata-static.plex.tv/0/people/0a7fc9968777eb53b804b4869021b4c1.jpg" />
<Role id="282757" filter="actor=282757" tag="Gabriela Ca&#322;un" tagKey="5d7769597a53e9001e6e388f" role="Russian Maid" thumb="https://metadata-static.plex.tv/3/people/3b3206ea29cdbd5da9d4afd903d9e367.jpg" />
<Role id="271672" filter="actor=271672" tag="Gabriel Constantin" tagKey="5d77699a47dd6e001f6c7b3c" role="Russian Master of Ceremonies" thumb="https://metadata-static.plex.tv/people/5d77699a47dd6e001f6c7b3c.jpg" />
<Role id="292773" filter="actor=292773" tag="V&#229;r Haugholt" tagKey="5f3fd32204a86500409843d9" role="Russian Prostitute #1" thumb="https://metadata-static.plex.tv/7/people/77c955c934e25c553ec706550f18e0d6.jpg" />
<Role id="292772" filter="actor=292772" tag="Ronja Haugholt" tagKey="5f3fd2fde4fc61003700cfa3" role="Russian Prostitute #2" thumb="https://metadata-static.plex.tv/2/people/277dfdf98b4f618e0320d38ebf4ee2d5.jpg" />
<Role id="292771" filter="actor=292771" tag="Alyona Kazarova" tagKey="5d7768b21999bc0020dce3ed" role="Yusupov Guest #1" />
<Role id="282756" filter="actor=282756" tag="Fiz Marcus" tagKey="5d77685c6f4521001eaa35e5" role="Yusupov Guest #2" thumb="https://image.tmdb.org/t/p/original/weXBX8Z7SYcWWeEiQ1IZ0GJhpxM.jpg" />
<Role id="292770" filter="actor=292770" tag="Nina Novich" tagKey="5d776eb623d5a3001f52f6dd" role="Yusupov Guest #3" />
<Role id="292769" filter="actor=292769" tag="Andrey Andreev" tagKey="6003efb91bcc9e002c77bf22" role="Yusupov Guest #4" thumb="https://metadata-static.plex.tv/6/people/6d7b0bcf64d22f4362799fab93526023.jpg" />
<Role id="165657" filter="actor=165657" tag="August Diehl" tagKey="5d776826961905001eb90df5" role="Vladimir Lenin" thumb="https://metadata-static.plex.tv/3/people/317ae6d40219be26340a7c2b70532d14.jpg" />
<Role id="282750" filter="actor=282750" tag="Nigel Lister" tagKey="5f3fe488bf3e560040b2df7c" role="Arthur Zimmermann" />
<Role id="282754" filter="actor=282754" tag="Daniel Vernan" tagKey="5f402aaece2564003f8eb5ba" role="German Foreign Office Worker #1" />
<Role id="218469" filter="actor=218469" tag="Nigel Pilkington" tagKey="5d7768264de0ee001fcc88ce" role="German Foreign Office Worker #2" thumb="https://metadata-static.plex.tv/e/people/ee6d0f36e383a64f844375694a991f9b.jpg" />
<Role id="271663" filter="actor=271663" tag="Ed Cooper Clarke" tagKey="5d776a399ab54400214fc602" role="Admiralty Military Intel Officer" thumb="https://metadata-static.plex.tv/people/5d776a399ab54400214fc602.jpg" />
<Role id="265440" filter="actor=265440" tag="Stevee Davies" tagKey="5d7768ca0ea56a001e2aa4b6" role="Young Codebreaker" thumb="https://metadata-static.plex.tv/people/5d7768ca0ea56a001e2aa4b6.jpg" />
<Role id="198550" filter="actor=198550" tag="Alison Steadman" tagKey="5d776835151a60001f24db7e" role="Rita" thumb="https://metadata-static.plex.tv/a/people/a57c06694a9d3422e120c98c5860ca72.jpg" />
<Role id="165674" filter="actor=165674" tag="Russell Balogh" tagKey="5d7768e7ad5437001f75249a" role="Sandhurst PT" thumb="https://metadata-static.plex.tv/7/people/7df43dea60ee172445f6eddc7bd5ac8f.jpg" />
<Role id="406546" filter="actor=406546" tag="Kristian Nekrasov" tagKey="5d77695d47dd6e001f6c463f" role="General Ludendorff" thumb="https://metadata-static.plex.tv/9/people/94ac8fb1340c95d92bea90f08c550b11.jpg" />
<Role id="271661" filter="actor=271661" tag="Stefan Schiffer" tagKey="624713230cb2a0fedb1613c4" role="Ludendorff Butler" />
<Role id="184026" filter="actor=184026" tag="Tim Bruce" tagKey="5d77699dfb0d55001f52af0f" role="Sandhurst Chaplain" />
<Role id="271660" filter="actor=271660" tag="Hal Hillman" tagKey="5e1656a910faa500400fcafe" role="Sandhurst Cadet" />
<Role id="185803" filter="actor=185803" tag="Ian Kelly" tagKey="5d7768395af944001f1fb101" role="President Woodrow Wilson" thumb="https://metadata-static.plex.tv/people/5d7768395af944001f1fb101.jpg" />
<Role id="292762" filter="actor=292762" tag="David Calvitto" tagKey="5f3ff460b8a032003d83bcd8" role="Vice President" />
<Role id="174664" filter="actor=174664" tag="Ian Porter" tagKey="5d7768286f4521001ea99431" role="General" thumb="https://metadata-static.plex.tv/people/5d7768286f4521001ea99431.jpg" />
<Role id="180393" filter="actor=180393" tag="Simon Connolly" tagKey="5d776b1f96b655001fe0518e" role="White House Butler" thumb="https://metadata-static.plex.tv/people/5d776b1f96b655001fe0518e.jpg" />
<Role id="271659" filter="actor=271659" tag="Alexander Cobb" tagKey="5d776a8d23d5a3001f505df1" role="British Officer" thumb="https://metadata-static.plex.tv/1/people/1396ed0b4d3414c42f5c5b69f54ccdbd.jpg" />
<Role id="167141" filter="actor=167141" tag="Aaron Taylor-Johnson" tagKey="5d77682a880197001ec9141f" role="Archie Reid" thumb="https://metadata-static.plex.tv/e/people/eef9440d80ff8364c8ede950ea4ff7e0.jpg" />
<Role id="208295" filter="actor=208295" tag="Emun Elliott" tagKey="5d7768761999bc0020dc57b0" role="Sergeant Major" thumb="https://metadata-static.plex.tv/e/people/ed6a3bed21c6f58a18896e6f95315d28.jpg" />
<Role id="282753" filter="actor=282753" tag="James Backway" tagKey="5f3ff252fea1a1003f9aa4aa" role="Soldier" thumb="https://image.tmdb.org/t/p/original/3tZas3TW230NQVI44LNao0Zi7ZP.jpg" />
<Role id="271657" filter="actor=271657" tag="Cassidy Little" tagKey="5d777046ad5437001f81e0ea" role="British Spy" thumb="https://metadata-static.plex.tv/people/5d777046ad5437001f81e0ea.jpg" />
<Role id="208484" filter="actor=208484" tag="Neil Jackson" tagKey="5d77682b151a60001f24b9fb" role="Captain Forrest" thumb="https://metadata-static.plex.tv/5/people/56a83b15cd544633302292bc5dbf9c92.jpg" />
<Role id="271656" filter="actor=271656" tag="Ben Ayers" tagKey="610fe6869931f1002c9b3691" role="Black Watch Soldier #1" />
<Role id="271655" filter="actor=271655" tag="Gwithian Evans" tagKey="6247132268958cfe880ade93" role="Black Watch Soldier #2" />
<Role id="271654" filter="actor=271654" tag="Cory Stuckey" tagKey="5d776c2047dd6e001f6e7411" role="Black Watch Soldier #3" />
<Role id="292767" filter="actor=292767" tag="Timon Staehler" tagKey="5f402df5fea1a1003fa0094d" role="Storm Trooper" />
<Role id="292766" filter="actor=292766" tag="Timothy Blore" tagKey="5f406c505a76a80042de5971" role="German Soldier #1" />
<Role id="265436" filter="actor=265436" tag="Ross Anderson" tagKey="5d776a5ead5437001f77ba13" role="Corporal Johnstone" thumb="https://metadata-static.plex.tv/4/people/49216e647b42046a2bf2cc3b86ef868a.jpg" />
<Role id="236122" filter="actor=236122" tag="Robert Aramayo" tagKey="5d7768c796b655001fdc17e1" role="Sergeant Major Atkins" thumb="https://metadata-static.plex.tv/a/people/a4afad16ee6c5c4998730de2eb5c826e.jpg" />
<Role id="292765" filter="actor=292765" tag="Remus Brooks" tagKey="60fa7917b92572002d3160b1" role="Kings Liverpool Soldier #1" />
<Role id="271650" filter="actor=271650" tag="Felix Mosse" tagKey="5d9f3580b0262f001f6eb937" role="Kings Liverpool Soldier #2" />
<Role id="292764" filter="actor=292764" tag="Will Pattle" tagKey="5f3fc644fea1a1003f96ad29" role="Kings Liverpool Soldier #3" />
<Role id="282752" filter="actor=282752" tag="Amy Leeson" tagKey="5f3fd7bcbf3e560040b1de76" role="Pub Girl #1" />
<Role id="292763" filter="actor=292763" tag="Dolores Carbonari" tagKey="5f3fc7b452f200004148e5d7" role="Pub Girl #2" thumb="https://metadata-static.plex.tv/b/people/bc0dabff3e51cec6ab59a3f41273b844.jpg" />
<Role id="170989" filter="actor=170989" tag="Stanley Tucci" tagKey="5d7768265af944001f1f668a" role="United States Ambassador" thumb="https://metadata-static.plex.tv/5/people/5ee4b741dfbb6947037a414aabf2029f.jpg" />
<Role id="271646" filter="actor=271646" tag="Pippa Winslow" tagKey="5d776aa196b655001fdf4581" role="United States Embassy Secretary" thumb="https://metadata-static.plex.tv/1/people/1eccbe091685c4bae6c39ab70ad3324d.jpg" />
<Role id="265450" filter="actor=265450" tag="David Kross" tagKey="5d7768255af944001f1f65c0" role="Moustached Man" thumb="https://metadata-static.plex.tv/e/people/e000ed6e0e55133ba1d146e5aa82213e.jpg" />
<Role id="265451" filter="actor=265451" tag="Katarina Martin" tagKey="5d777052dd931c001e38b39a" role="Housekeeper (uncredited)" thumb="https://metadata-static.plex.tv/2/people/29d12542f6e1aa185250126d7951156c.jpg" />
<Role id="265452" filter="actor=265452" tag="Kya Garwood" tagKey="5d776bb6594b2b001e6e1bad" role="Maid (uncredited)" thumb="https://metadata-static.plex.tv/b/people/bb3796535d88b03d74db2aeb2912baee.jpg" />
<Role id="184295" filter="actor=184295" tag="Constantine Gregory" tagKey="5d77682854c0f0001f301f79" role="Mayor of Sarajevo (uncredited)" thumb="https://metadata-static.plex.tv/people/5d77682854c0f0001f301f79.jpg" />
<Role id="212754" filter="actor=212754" tag="Hal Fowler" tagKey="5d7768fd96b655001fdc75bd" role="Russian General (uncredited)" thumb="https://metadata-static.plex.tv/7/people/771228c005f76e0a7ad7984a2df29fde.jpg" />
<Role id="186401" filter="actor=186401" tag="Renars Latkovskis" tagKey="5d776c2e51dd69001fe3884a" role="Russian Sheppard (uncredited)" thumb="https://metadata-static.plex.tv/0/people/00233c207114f5b0afca0539b6ab7d91.jpg" />
<Role id="265453" filter="actor=265453" tag="Jack Cunningham-Nuttall" tagKey="5d776c93ad5437001f7c244a" role="Bath Boy (uncredited)" thumb="https://metadata-static.plex.tv/8/people/8a0fe77e45116c39ba4b3ecf1581ca78.jpg" />
<Role id="265454" filter="actor=265454" tag="Chlo&#233; Booyens" tagKey="5d776c6747dd6e001f6ea9fa" role="Soldier (uncredited)" thumb="https://metadata-static.plex.tv/2/people/24d7046f82325898d71d9f475b04cef2.jpg" />
<Producer id="167999" filter="producer=167999" tag="Matthew Vaughn" tagKey="5d776826e6d55c002040af53" thumb="https://metadata-static.plex.tv/3/people/37809b0934d7ae73f85791903aa1dc9c.jpg" />
<Producer id="342031" filter="producer=342031" tag="David Reid" tagKey="5d77683454c0f0001f3035ba" />
<Producer id="190571" filter="producer=190571" tag="Adam Bohling" tagKey="5d77682ff59e580021897fd3" />
</Video>
</MediaContainer>""",
}
FILES_MATCHES = {
    "/library/metadata/73564/thumb/1743847562": "poster.jpg",
    "/library/metadata/73564/art/1743847562": "landscape.jpg",
}
EXPECTED_NFO = """<movie>
  <actors>
    <actor>
      <name>Ralph Fiennes</name>
      <role>Orlando Oxford</role>
      <order>0</order>
    </actor>
    <actor>
      <name>Gemma Arterton</name>
      <role>Polly</role>
      <order>1</order>
    </actor>
    <actor>
      <name>Rhys Ifans</name>
      <role>Grigori Rasputin</role>
      <order>2</order>
    </actor>
    <actor>
      <name>Matthew Goode</name>
      <role>Morton</role>
      <order>3</order>
    </actor>
    <actor>
      <name>Tom Hollander</name>
      <role>King George / Kaiser Wilhelm / Tsar Nicholas</role>
      <order>4</order>
    </actor>
    <actor>
      <name>Harris Dickinson</name>
      <role>Conrad Oxford</role>
      <order>5</order>
    </actor>
    <actor>
      <name>Daniel Brühl</name>
      <role>Erik Jan Hanussen</role>
      <order>6</order>
    </actor>
    <actor>
      <name>Djimon Hounsou</name>
      <role>Shola</role>
      <order>7</order>
    </actor>
    <actor>
      <name>Charles Dance</name>
      <role>Kitchener</role>
      <order>8</order>
    </actor>
    <actor>
      <name>Shaun McKee</name>
      <role>Camp Guard #1</role>
      <order>9</order>
    </actor>
    <actor>
      <name>Peter York</name>
      <role>Camp Guard #2</role>
      <order>10</order>
    </actor>
    <actor>
      <name>Alexandra Maria Lara</name>
      <role>Emily Oxford</role>
      <order>11</order>
    </actor>
    <actor>
      <name>Alexander Shaw</name>
      <role>Young Conrad</role>
      <order>12</order>
    </actor>
    <actor>
      <name>Bevan Viljoen</name>
      <role>Boer Sniper</role>
      <order>13</order>
    </actor>
    <actor>
      <name>Shaun Scott</name>
      <role>Kingsman Tailor #1</role>
      <order>14</order>
    </actor>
    <actor>
      <name>Andrew Bridgmont</name>
      <role>Kingsman Tailor #2</role>
      <order>15</order>
    </actor>
    <actor>
      <name>Olivier Richters</name>
      <role>Huge Machinery Shack Guard</role>
      <order>16</order>
    </actor>
    <actor>
      <name>Valerie Pachner</name>
      <role>Mata Hari</role>
      <order>17</order>
    </actor>
    <actor>
      <name>Joel Basman</name>
      <role>Gavrilo Princip</role>
      <order>18</order>
    </actor>
    <actor>
      <name>Todd Boyce</name>
      <role>Dupont</role>
      <order>19</order>
    </actor>
    <actor>
      <name>Richard Stephenson Winter</name>
      <role>Shepherd's Flock Member #2</role>
      <order>20</order>
    </actor>
    <actor>
      <name>Takako Akashi</name>
      <role>Shepherd's Flock Member #3</role>
      <order>21</order>
    </actor>
    <actor>
      <name>Thorston Manderlay</name>
      <role>Shepherd's Flock Member #4</role>
      <order>22</order>
    </actor>
    <actor>
      <name>Terence Anderson</name>
      <role>Shepherd's Flock Member #5</role>
      <order>23</order>
    </actor>
    <actor>
      <name>Andy Cheung</name>
      <role>Shepherd's Flock Member #6</role>
      <order>24</order>
    </actor>
    <actor>
      <name>Ron Cook</name>
      <role>Archduke Franz Ferdinand of Austria</role>
      <order>25</order>
    </actor>
    <actor>
      <name>Barbara Drennan</name>
      <role>Sophie, Duchess of Hohenberg</role>
      <order>26</order>
    </actor>
    <actor>
      <name>Maja Simonsen</name>
      <role>Pretty Girl</role>
      <order>27</order>
    </actor>
    <actor>
      <name>Benedick Blythe</name>
      <role>Saravejo General</role>
      <order>28</order>
    </actor>
    <actor>
      <name>Max Count</name>
      <role>Young King George</role>
      <order>29</order>
    </actor>
    <actor>
      <name>Emil Oksanen</name>
      <role>Young Kaiser Wilhelm</role>
      <order>30</order>
    </actor>
    <actor>
      <name>George Gooderham</name>
      <role>Young Tsar Nicholas</role>
      <order>31</order>
    </actor>
    <actor>
      <name>Alexa Povah</name>
      <role>Queen Victoria</role>
      <order>32</order>
    </actor>
    <actor>
      <name>Branka Katić</name>
      <role>Tsarina Alix</role>
      <order>33</order>
    </actor>
    <actor>
      <name>Alexander Shefler</name>
      <role>Tsarevich Alexei</role>
      <order>34</order>
    </actor>
    <actor>
      <name>Rosie Goddard</name>
      <role>Grand Duchess Anastasia</role>
      <order>35</order>
    </actor>
    <actor>
      <name>Dora Davis</name>
      <role>Grand Duchess Maria</role>
      <order>36</order>
    </actor>
    <actor>
      <name>Lucia Jade Barker</name>
      <role>Grand Duchess Olga</role>
      <order>37</order>
    </actor>
    <actor>
      <name>Molly McGeachin</name>
      <role>Grand Duchess Tatiana</role>
      <order>38</order>
    </actor>
    <actor>
      <name>Angus Castle-Doughty</name>
      <role>British Soldier</role>
      <order>39</order>
    </actor>
    <actor>
      <name>Jed O'Hagan</name>
      <role>British Soldier #2</role>
      <order>40</order>
    </actor>
    <actor>
      <name>Thomas Mahy</name>
      <role>British Soldier #3</role>
      <order>41</order>
    </actor>
    <actor>
      <name>Connor Calland</name>
      <role>British Soldier #4</role>
      <order>42</order>
    </actor>
    <actor>
      <name>James Musgrave</name>
      <role>Lieutenant</role>
      <order>43</order>
    </actor>
    <actor>
      <name>Martin Razpopov</name>
      <role>Sarajevo Prison Warden</role>
      <order>44</order>
    </actor>
    <actor>
      <name>Aaron Vodovoz</name>
      <role>Felix Yusupov</role>
      <order>45</order>
    </actor>
    <actor>
      <name>Gabriela Całun</name>
      <role>Russian Maid</role>
      <order>46</order>
    </actor>
    <actor>
      <name>Gabriel Constantin</name>
      <role>Russian Master of Ceremonies</role>
      <order>47</order>
    </actor>
    <actor>
      <name>Vår Haugholt</name>
      <role>Russian Prostitute #1</role>
      <order>48</order>
    </actor>
    <actor>
      <name>Ronja Haugholt</name>
      <role>Russian Prostitute #2</role>
      <order>49</order>
    </actor>
    <actor>
      <name>Alyona Kazarova</name>
      <role>Yusupov Guest #1</role>
      <order>50</order>
    </actor>
    <actor>
      <name>Fiz Marcus</name>
      <role>Yusupov Guest #2</role>
      <order>51</order>
    </actor>
    <actor>
      <name>Nina Novich</name>
      <role>Yusupov Guest #3</role>
      <order>52</order>
    </actor>
    <actor>
      <name>Andrey Andreev</name>
      <role>Yusupov Guest #4</role>
      <order>53</order>
    </actor>
    <actor>
      <name>August Diehl</name>
      <role>Vladimir Lenin</role>
      <order>54</order>
    </actor>
    <actor>
      <name>Nigel Lister</name>
      <role>Arthur Zimmermann</role>
      <order>55</order>
    </actor>
    <actor>
      <name>Daniel Vernan</name>
      <role>German Foreign Office Worker #1</role>
      <order>56</order>
    </actor>
    <actor>
      <name>Nigel Pilkington</name>
      <role>German Foreign Office Worker #2</role>
      <order>57</order>
    </actor>
    <actor>
      <name>Ed Cooper Clarke</name>
      <role>Admiralty Military Intel Officer</role>
      <order>58</order>
    </actor>
    <actor>
      <name>Stevee Davies</name>
      <role>Young Codebreaker</role>
      <order>59</order>
    </actor>
    <actor>
      <name>Alison Steadman</name>
      <role>Rita</role>
      <order>60</order>
    </actor>
    <actor>
      <name>Russell Balogh</name>
      <role>Sandhurst PT</role>
      <order>61</order>
    </actor>
    <actor>
      <name>Kristian Nekrasov</name>
      <role>General Ludendorff</role>
      <order>62</order>
    </actor>
    <actor>
      <name>Stefan Schiffer</name>
      <role>Ludendorff Butler</role>
      <order>63</order>
    </actor>
    <actor>
      <name>Tim Bruce</name>
      <role>Sandhurst Chaplain</role>
      <order>64</order>
    </actor>
    <actor>
      <name>Hal Hillman</name>
      <role>Sandhurst Cadet</role>
      <order>65</order>
    </actor>
    <actor>
      <name>Ian Kelly</name>
      <role>President Woodrow Wilson</role>
      <order>66</order>
    </actor>
    <actor>
      <name>David Calvitto</name>
      <role>Vice President</role>
      <order>67</order>
    </actor>
    <actor>
      <name>Ian Porter</name>
      <role>General</role>
      <order>68</order>
    </actor>
    <actor>
      <name>Simon Connolly</name>
      <role>White House Butler</role>
      <order>69</order>
    </actor>
    <actor>
      <name>Alexander Cobb</name>
      <role>British Officer</role>
      <order>70</order>
    </actor>
    <actor>
      <name>Aaron Taylor-Johnson</name>
      <role>Archie Reid</role>
      <order>71</order>
    </actor>
    <actor>
      <name>Emun Elliott</name>
      <role>Sergeant Major</role>
      <order>72</order>
    </actor>
    <actor>
      <name>James Backway</name>
      <role>Soldier</role>
      <order>73</order>
    </actor>
    <actor>
      <name>Cassidy Little</name>
      <role>British Spy</role>
      <order>74</order>
    </actor>
    <actor>
      <name>Neil Jackson</name>
      <role>Captain Forrest</role>
      <order>75</order>
    </actor>
    <actor>
      <name>Ben Ayers</name>
      <role>Black Watch Soldier #1</role>
      <order>76</order>
    </actor>
    <actor>
      <name>Gwithian Evans</name>
      <role>Black Watch Soldier #2</role>
      <order>77</order>
    </actor>
    <actor>
      <name>Cory Stuckey</name>
      <role>Black Watch Soldier #3</role>
      <order>78</order>
    </actor>
    <actor>
      <name>Timon Staehler</name>
      <role>Storm Trooper</role>
      <order>79</order>
    </actor>
    <actor>
      <name>Timothy Blore</name>
      <role>German Soldier #1</role>
      <order>80</order>
    </actor>
    <actor>
      <name>Ross Anderson</name>
      <role>Corporal Johnstone</role>
      <order>81</order>
    </actor>
    <actor>
      <name>Robert Aramayo</name>
      <role>Sergeant Major Atkins</role>
      <order>82</order>
    </actor>
    <actor>
      <name>Remus Brooks</name>
      <role>Kings Liverpool Soldier #1</role>
      <order>83</order>
    </actor>
    <actor>
      <name>Felix Mosse</name>
      <role>Kings Liverpool Soldier #2</role>
      <order>84</order>
    </actor>
    <actor>
      <name>Will Pattle</name>
      <role>Kings Liverpool Soldier #3</role>
      <order>85</order>
    </actor>
    <actor>
      <name>Amy Leeson</name>
      <role>Pub Girl #1</role>
      <order>86</order>
    </actor>
    <actor>
      <name>Dolores Carbonari</name>
      <role>Pub Girl #2</role>
      <order>87</order>
    </actor>
    <actor>
      <name>Stanley Tucci</name>
      <role>United States Ambassador</role>
      <order>88</order>
    </actor>
    <actor>
      <name>Pippa Winslow</name>
      <role>United States Embassy Secretary</role>
      <order>89</order>
    </actor>
    <actor>
      <name>David Kross</name>
      <role>Moustached Man</role>
      <order>90</order>
    </actor>
    <actor>
      <name>Katarina Martin</name>
      <role>Housekeeper (uncredited)</role>
      <order>91</order>
    </actor>
    <actor>
      <name>Kya Garwood</name>
      <role>Maid (uncredited)</role>
      <order>92</order>
    </actor>
    <actor>
      <name>Constantine Gregory</name>
      <role>Mayor of Sarajevo (uncredited)</role>
      <order>93</order>
    </actor>
    <actor>
      <name>Hal Fowler</name>
      <role>Russian General (uncredited)</role>
      <order>94</order>
    </actor>
    <actor>
      <name>Renars Latkovskis</name>
      <role>Russian Sheppard (uncredited)</role>
      <order>95</order>
    </actor>
    <actor>
      <name>Jack Cunningham-Nuttall</name>
      <role>Bath Boy (uncredited)</role>
      <order>96</order>
    </actor>
    <actor>
      <name>Chloé Booyens</name>
      <role>Soldier (uncredited)</role>
      <order>97</order>
    </actor>
  </actors>
  <country>United Kingdom</country>
  <country>United States of America</country>
  <dateadded>2025-04-05 10:05:17</dateadded>
  <lastplayed>2022-02-24 21:15:06</lastplayed>
  <originalTitle>The King's Man</originalTitle>
  <playcount>1</playcount>
  <watched>true</watched>
  <plot>En 1902, l'aristocrate Orlando, duc d'Oxford, perd sa femme Emily lors d'une mission humanitaire en Afrique du Sud lors de la seconde guerre des Boers ; leur jeune fils Conrad assiste lui aussi à sa mort. Douze ans plus tard, le pacifiste convaincu Orlando sent qu'un conflit mondial menace. Il tente par ailleurs de dissuader son fils, âgé de 18 ans, de s'engager dans l'armée britannique. Il a imploré son grand ami, le secrétaire d'État à la Guerre Horatio Herbert Kitchener, de bloquer sa demande d'incorporation. Aidé par ses domestiques Shola et Polly, le duc a par ailleurs créé un réseau d'espionnage mondial et se renseigne sur la menace qui plane sur l'Europe. En effet, dans l'ombre, une mystérieuse organisation souhaite renverser l'ordre mondial.</plot>
  <releasedate>2021-12-22</releasedate>
  <premiereda>2021-12-22</premiereda>
  <runtime>130</runtime>
  <sorttitle>King's Man : Premiere Mission</sorttitle>
  <studio>Marv</studio>
  <tagline>Découvrez les origines de la toute première agence de renseignement indépendante.</tagline>
  <title>The King's Man : Première Mission</title>
  <uniqueid type="imdb" default="true">tt6856242</uniqueid>
  <id>tt6856242</id>
  <imdbid>tt6856242</imdbid>
  <uniqueid type="tmdb">476669</uniqueid>
  <tmdbid>476669</tmdbid>
  <uniqueid type="tvdb">9846</uniqueid>
  <tvdbid>9846</tvdbid>
  <year>2021</year>
  <mpaa>R</mpaa>
  <ratings>
    <rating name="imdb" max="10" default="true">
      <value>6.300000</value>
    </rating>
    <rating name="rottentomatoes" max="10">
      <value>8.000000</value>
    </rating>
    <rating name="themoviedb" max="10">
      <value>6.800000</value>
    </rating>
  </ratings>
  <writer>Matthew Vaughn</writer>
  <writer>Karl Gajdusek</writer>
  <writer>Mark Millar</writer>
  <writer>Dave Gibbons</writer>
  <director>Matthew Vaughn</director>
  <genre>Action</genre>
  <genre>Adventure</genre>
  <genre>Thriller</genre>
  <genre>Drame</genre>
  <genre>Histoire</genre>
</movie>"""

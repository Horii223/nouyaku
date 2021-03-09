import streamlit as st


st.header('HIDDEN')
st.subheader('これは昔から伝わるHIDDENの薬...')

crop_class =st.selectbox(
"今回の作物分類は",
    ('下から選択して下さい','稲','麦類','はとむぎ','豆類','とうもろこし','てんさい','芋類','果樹類',
    'サトウキビ','樹木類','野菜類','飼料作物','芝','その他')
    )
###################################################
def ine_name():
    ine_name =st.selectbox(
    "水稲の種類は",
    ("直播水稲","移植水稲")
    )
    if ine_name =="直播水稲":
        ine_direct()
    elif ine_name =="移植水稲":
        ine_trans_joso()
def ine_direct():
        ine_direct = st.selectbox(
        '使用用途は',
        ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
        )
        if ine_direct == "除草剤":
            ine_direct_joso()
        if ine_direct =="殺菌剤":
            ine_direct_kin ()
        if ine_direct =="殺虫剤":
            ine_direct_insect()
        if ine_direct =="殺菌殺虫剤":
            ine_direct_insectkin()
        if ine_direct =="農薬肥料":
            ine_direct_felt()
        if ine_direct =="植物成長調整剤":
            ine_direct_grow()
def ine_direct_grow():
        ine_direct_grow=st.selectbox(
        "名前は",
        ("石原スマレクト粒剤","ビビフルフロアブル","カルパー粉粒剤１６","カヤクカルパー粉粒剤１６")
        )
        ine_name = st.selectbox(
        '今回の作物名は',
        ('下から選択して下さい','移植水稲','直播水稲')
        )
def ine_direct_joso():
        ine_direct_joso=st.selectbox(
         "名前は",
         ('ＨＣＣキックバイ１キロ粒剤', 'ＪＡエーワン１キロ粒剤', 'ＪＡエーワンフロアブル', 'ＯＡＴスマートフロアブル',
         'ＳＤＳイザナギ１キロ粒剤', 'ＳＤＳイザナギフロアブル', 'ＳＤＳカイシＭＦ１キロ粒剤', 'ＳＤＳキックバイ１キロ粒剤',
         'ＳＤＳハイカット１キロ粒剤', 'ＳＤＳブルゼータ１キロ粒剤', 'ＳＤＳ月光１キロ粒剤', 'アールタイプ１キロ粒剤',
         'アールタイプフロアブル', 'アクシズＭＸ１キロ粒剤', 'アグロスクリンチャー１キロ粒剤', 'アシュラ１キロ粒剤',
         'アシュラ４００ＦＧ', 'アシュラフロアブル', 'アットウＺ１キロ粒剤', 'アットウＺ４００ＦＧ', 'アットウＺフロアブル',
         'アッパレＺ１キロ粒剤', 'アッパレＺ４００ＦＧ', 'アトトリ１キロ粒剤', 'アトトリ豆つぶ２５０', 'アネシス１キロ粒剤',
         'アバンティ１キロ粒剤', 'アバンティフロアブル', 'アピログロウＭＸエアー粒剤', 'アルファープロ１キロ粒剤７５',
         'アルファープロＬ豆つぶ２５０', 'イザナギ１キロ粒剤', 'イザナギフロアブル', 'イッソウ１キロ粒剤',
         'イネキング１キロ粒剤', 'イネキングフロアブル', 'イネヒーロー１キロ粒剤', 'ウィナー１キロ粒剤５１',
         'ウィナー１キロ粒剤７５', 'ウィナーＬフロアブル', 'ウィナーフロアブル', 'ウィニングラン１キロ粒剤',
         'ウィニングランフロアブル', 'ウルティモＺ１キロ粒剤', 'ウルティモＺフロアブル', 'エンペラー豆つぶ２５０',
         'オーリック１キロ粒剤', 'オサキニ１キロ粒剤', 'オシオキＭＸ１キロ粒剤', 'オテゴロ１キロ粒剤',
         'オマージュＺ１キロ粒剤', 'オマージュＺフロアブル', 'カイシＭＦ１キロ粒剤', 'カウンシルエナジー１キロ粒剤',
         'カウンシルエナジーフロアブル', 'カウンシルコンプリート１キロ粒剤', 'カウンシルコンプリートフロアブル',
         'カウントダウン１キロ粒剤', 'カウントダウンフロアブル', 'カチボシ１キロ粒剤５１', 'カチボシ１キロ粒剤７５',
         'カチボシＬフロアブル', 'カチボシフロアブル', 'カリュード１キロ粒剤', 'カリュードフロアブル', 'ガンガン１キロ粒剤',
         'ガンガン豆つぶ２５０', 'キクンジャーＺ１キロ粒剤', 'キックバイ１キロ粒剤', 'キマリテ１キロ粒剤',
         'キマリテフロアブル', 'キラリ１キロ粒剤', 'クサウェポン１キロ粒剤', 'クサウェポンフロアブル',
         'クサトリーＢＳＸ１キロ粒剤５１', 'クサバルカン１キロ粒剤', 'クサバルカンフロアブル', 'クミスター１キロ粒剤７５',
         'クミスターＬ豆つぶ２５０', 'クリンチャー１キロ粒剤', 'クレセントフロアブル', 'クレバールＺ１キロ粒剤',
         'クレバールＺフロアブル', 'ゲパード１キロ粒剤', 'ゲパードエアー粒剤', 'ゴウワン１キロ粒剤５１',
         'ゴエモン１キロ粒剤', 'コメット１キロ粒剤', 'コメット顆粒', 'サスケ粒剤２００', 'サファイア１キロ粒剤',
         'サラブレッドＫＡＩ１キロ粒剤', 'サラブレッドＫＡＩ４００ＦＧ', 'サラブレッドＫＡＩフロアブル',
         'サンバード１キロ粒剤３０', 'サンバード粒剤', 'サンパンチ１キロ粒剤', 'シアゲＭＦ１キロ粒剤',
         'ジェイソウル１キロ粒剤', 'ジェイソウルフロアブル', 'ジェイフレンド１キロ粒剤', 'ジェイフレンド４００ＦＧ',
         'ジカマック５００グラム粒剤', 'シグナス１キロ粒剤', 'シグナスエアー粒剤', 'シグナスフロアブル',
         'ジャイブスカイ５００グラム粒剤', 'ジャイロ１キロ粒剤', 'ジャイロフロアブル', 'ジャスタ１キロ粒剤',
         'ジャスタフロアブル', 'ジャンダルムＭＸ１キロ粒剤', 'ジャンダルムＭＸ豆つぶ２５０', 'シュナイデン１キロ粒剤',
         'シュナイデンフロアブル', 'シンズイＺ豆つぶ２５０', 'スケダチエース１キロ粒剤', 'スマートフロアブル',
         'ゼータタイガー１キロ粒剤', 'ゼータタイガー３００ＦＧ', 'ゼータタイガーフロアブル', 'ゼータハンマー１キロ粒剤',
         'ゼータハンマーフロアブル', 'ゼータファイヤ１キロ粒剤', 'センイチＭＸ１キロ粒剤',
         'タンボエースＫ3000Ｚ１キロ粒剤', 'タンボエーススカイ５００グラム粒剤', 'タンボパワー１キロ粒剤',
         'ツルギ１キロ粒剤', 'ツルギ２５０粒剤', 'ツルギフロアブル', 'ディオーレ１キロ粒剤', 'ディオーレエアー粒剤',
         'テイクイット１キロ粒剤', 'テイクイットフロアブル', 'テッケン１キロ粒剤', 'デルタアタック１キロ粒剤',
         'デルタアタック４００ＦＧ', 'デルタアタックフロアブル', 'トップガン２５０グラム', 'トップガンＬ２５０グラム',
         'トップガンＲ豆つぶ２５０', 'トドメＭＦ１キロ粒剤', 'ドニチＳ１キロ粒剤', 'ドラゴンホークＺ１キロ粒剤',
         'ドラゴンホークＺ３００ＦＧ', 'ドラゴンホークＺフロアブル', 'ドリフ１キロ粒剤', 'ドンピシャ１キロ粒剤',
         'ナギナタ豆つぶ２５０', 'ニトウリュウ１キロ粒剤', 'ニマイメＺ１キロ粒剤', 'ニマイメＺフロアブル',
         'ハイカット１キロ粒剤', 'バイスコープ１キロ粒剤', 'バッチリ１キロ粒剤', 'バッチリ４００ＦＧ',
         'バッチリＬＸ１キロ粒剤', 'バッチリＬＸ４００ＦＧ', 'バッチリＬＸフロアブル', 'ヒエクッパエース１キロ粒剤',
         'ヒエクリーン１キロ粒剤', 'ヒエクリーン豆つぶ２５０', 'ビクトリーＺ１キロ粒剤', 'ビクトリーＺ４００ＦＧ',
         'ビクトリーＺフロアブル', 'ビッグシュアＺ１キロ粒剤５１', 'ピラクロエース１キロ粒剤', 'ピラクロエースフロアブル',
         'ピラクロン１キロ粒剤', 'フォローアップ１キロ粒剤', 'プライオリティフロアブル', 'プライオリティ豆つぶ２５０',
         'フルイニングスカイ５００グラム粒剤', 'フルスコアＺ１キロ粒剤', 'ブルゼータ１キロ粒剤',
         'フルチャージスカイ５００グラム粒剤', 'フルパワーＭＸ１キロ粒剤', 'フルパワーＭＸ５００グラムＦＧ',
         'プレキープ１キロ粒剤', 'プレキープフロアブル', 'ベストコンビスカイ５００グラム粒剤', 'ベストパートナー豆つぶ２５０',
         'ベッカク豆つぶ２５０', 'ベルーガ豆つぶ２５０', 'ベンケイ１キロ粒剤', 'ベンケイ豆つぶ２５０',
         'ホクコーエーワン１キロ粒剤', 'ホクコーエーワンフロアブル', 'ホクコークリンチャー１キロ粒剤',
         'ホクコーミスターホームラン１キロ粒剤５１', 'ホクコーミスターホームランＬフロアブル', 'ホクサンジャスタ１キロ粒剤',
         'ホクサンジャスタフロアブル', 'ボデーガード１キロ粒剤', 'ボデーガードプロ１キロ粒剤', 'ボデーガードフロアブル',
         'ボデーガードプロフロアブル', 'マキビシＺ１キロ粒剤', 'マクダス１キロ粒剤', 'マスラオ１キロ粒剤',
         'マスラオフロアブル', 'ミスターホームラン１キロ粒剤５１', 'ミスターホームランＬフロアブル', 'ムソウ豆つぶ２５０',
         'メガゼータ１キロ粒剤', 'メガゼータ４００ＦＧ', 'メガゼータフロアブル', 'モゲトン粒剤', 'ヤブサメ豆つぶ２５０',
         'リボルバー１キロ粒剤', 'リボルバーエース１キロ粒剤', 'ルナクロス１キロ粒剤', 'レイトリックＺ１キロ粒剤',
         'レイトリックＺフロアブル', 'レブラス１キロ粒剤', 'レブラスエアー粒剤', 'ワイドアタックＤ１キロ粒剤',
         'ワイドショット１キロ粒剤', 'ワンステージ１キロ粒剤', '協友マメットＳＭ１キロ粒剤', '銀河１キロ粒剤',
         '月光１キロ粒剤', '兆１キロ粒剤', '天空１キロ粒剤', '天空エアー粒剤', '天空フロアブル',
         '日産イネヒーロー１キロ粒剤', '日産クリンチャー１キロ粒剤', '日農イッポン１キロ粒剤７５',
         '日農イッポンＤ１キロ粒剤５１', '日農イッポンフロアブル', '忍１キロ粒剤', '忍フロアブル', '流星１キロ粒剤','流星エアー粒剤')
         )
        if ine_direct_joso =="ＪＡエーワン１キロ粒剤":
             call()
def ine_direct_kin():
        ine_direct_kin=st.selectbox(
        "名前は",
        ('ＪＡアミスターエイト', 'ＳＴビームエイトゾル', 'ＳＴビームゾル', 'アミスターエイト', 'オリゼメート粒剤２０',
           'オリゼメート粒剤４０', 'オリブライト１キロ粒剤', 'オリブライト２５０Ｇ', 'カスラブサイドゾル',
           'クミアイオリブライト２５０Ｇ', 'クミアイコラトップ１キロ粒剤１２', 'クミアイコラトップ粒剤２４',
           'クミアイトライフロアブル', 'クミアイビームエイトゾル', 'クミアイビームゾル', 'ゴウケツ１キロ粒剤',
           'ゴウケツ粒剤５００', 'コラトップ１キロ粒剤１２', 'コラトップ粒剤２４', 'サンブラス１キロ粒剤',
           'サンブラス粒剤１８', 'ダブルカットバリダフロアブル', 'ダブルカットフロアブル', 'トップジンＭゾル',
           'トライフロアブル', 'ノンブラスバリダフロアブル', 'ノンブラスフロアブル', 'バシタックゾル', 'バリダシンエアー',
           'ビームエイトゾル', 'ビームエイトモンカットフロアブル', 'ビームゾル', 'ビームバリダゾル', 'フジワン１キロ粒剤',
           'フジワン乳剤', 'ブラシンゾル', 'ブラシンバリダゾル', 'ブラステクトフロアブル', 'ホクコーオリゼメート粒剤２０',
           'ホクコーオリゼメート粒剤４０', 'ホクコーカスミンバリダシン液剤', 'ホクコーカスミン液剤', 'ホクコートップジンＭゾル',
           'ホクコーバリダシンエアー', 'ホクコーブラシンゾル', 'ホクコーブラシンバリダゾル', 'ホクコーラブサイドフロアブル',
           'モンカット１キロ粒剤２１', 'モンカットフロアブル', 'モンカットラブサイド２０フロアブル', 'モンガリット１キロ粒剤',
           'モンセレンフロアブル', 'ラブサイドバリダフロアブル', 'ラブサイドフロアブル', '協友アミスターエイト',
           '協友モンセレンフロアブル', '協友ラブサイドフロアブル', '協友ラブサイドモンセレンフロアブル',
           '日産モンカットフロアブル')
        )
def ine_direct_insect():
        ine_direct_insect=st.selectbox(
        "名前は",
        ('ＭＩＣマトリックフロアブル', 'ＭＲ．ジョーカーＥＷ', 'Ｎスクミンベイト３', 'ＳＴ\u3000ＭＲ．ジョーカーＥＷ',
           'アプロードスタークルゾル', 'アプロードゾル', 'エクシードフロアブル', 'エミリアフロアブル',
           'キラップジョーカーフロアブル', 'キラップフロアブル', 'クミアイアプロードスタークルゾル', 'クミアイエミリアフロアブル',
           'クミアイスミチオン乳剤', 'サンケイスミチオンＭＣ', 'サンケイスミチオン乳剤', 'スクミンブルー', 'スクミンベイト３',
           'スタークル１キロＨ粒剤', 'スタークルエアー５０', 'スタークルメイト１キロＨ粒剤', 'スタークルメイトエアー５０',
           'スタークルメイト液剤１０', 'スタークル液剤１０', 'スタートレボンＷ１０', 'スミチオンＭＣ', 'スミバッサＭＣ',
           'ダントツＥＸフロアブル', 'ダントツフロアブル', 'チューンアップ顆粒水和剤', 'トレボンエアー', 'トレボンスカイＭＣ',
           'トレボンスターフロアブル', 'ファームスター顆粒水溶剤５０', 'ホクコーＭＲ．ジョーカーＥＷ',
           'ホクコーエクシードフロアブル', 'ホクコーキラップジョーカーフロアブル', 'ホクコーキラップフロアブル',
           'ホクコースミチオン乳剤', 'ホクコーロムダンエアー', 'ホクサンスミチオン乳剤', 'マトリックフロアブル',
           'メタレックスＲＧ粒剤', 'ランナーフロアブル', 'ロムダンエアー', '一農スミチオン乳剤', '協友スミチオントレボン乳剤',
           '協友スミチオン乳剤', '協友ダントツフロアブル', '兼商チューンアップ顆粒水和剤', '住化スミチオン乳剤',
           '日産エクシードフロアブル', '日産スミチオン乳剤', '日農スミチオン乳剤', '日農メタレックスＲＧ粒剤',
           '日農ロムダンエアー', '理研スミチオン乳剤')
        )
def ine_direct_insectkin():
        ine_direct_insectkin=st.selectbox(
        "名前は",
        ('ＳＴビームエイトトレボンゾル', 'アプロードモンカットエアー', 'アプロードロムダンモンカットエアー',
           'アミスターアクタラＳＣ', 'アミスタートレボンＳＥ', 'イモチエーススタークル１キロ粒剤',
           'クミアイビームエイトトレボンゾル', 'クミアイビームキラップジョーカーフロアブル', 'ゲットワンエースフロアブル',
           'コラトップスタークル１キロ粒剤', 'シンジェンタアミスタートレボンＳＥ', 'ダブルアローＳＥ', 'ダブルカットＪフロアブル',
           'ダブルカットＫフロアブル', 'ダブルカットエクシードフロアブル', 'ダブルカットスタークルフロアブル',
           'ダブルカットトレボンフロアブル', 'トライＫフロアブル', 'トライトラムフロアブル', 'ノンブラスダントツフロアブル',
           'ノンブラスバリダダントツフロアブル', 'ビームエイトＥＸゾル', 'ビームエイトエクシードゾル',
           'ビームエイトスタークルゾル', 'ビームキラップジョーカーフロアブル', 'フジワンラップ粒剤', 'ブラシンキラップフロアブル',
           'ブラシンジョーカーフロアブル', 'ブラシンダントツフロアブル', 'ブラシンバリダダントツフロアブル',
           'ブレードスタークルゾル', 'ホクコーイモチエーススタークル１キロ粒剤', 'ホクコーカスラブバリダジョーカーフロアブル',
           'ホクコートップジンスタークルフロアブル', 'ホクコーブラシンキラップフロアブル', 'ホクコーブラシンジョーカーフロアブル',
           'ホクコーラブサイドキラップフロアブル', 'ホクコーラブサイドジョーカーフロアブル', 'ホクコーラブサイドスタークルフロアブル',
           'ホクコーラブサイドトレボンゾル１７', 'ラブサイドダントツフロアブル', '協友アミスターアクタラＳＣ')
        )
def ine_direct_felt():
        ine_direct_felt=st.selectbox(
        "名前は",
        ("スミショート１４","コープショート１４")
        )
def ine_trans_joso():
        ine_trans_joso=st.selectbox(
        "現在、除草剤のみ使用できます。",
        ('［ＤＩＣ］アワードフロアブル', '［ＤＩＣ］カルショットフロアブル', 'ＪＡエーワン１キロ粒剤', 'ＪＡエーワンフロアブル',
           'ＭＩＣカルショットフロアブル', 'ＭＩＣスウィープフロアブル', 'ＯＡＴスマートフロアブル', 'ＳＤＳアワードフロアブル',
           'ＳＤＳイザナギ１キロ粒剤', 'ＳＤＳイザナギフロアブル', 'ＳＤＳイッテツフロアブル', 'ＳＤＳオークスフロアブル',
           'ＳＤＳクラッシュ１キロ粒剤', 'ＳＤＳダブルスターＳＢ顆粒', 'ＳＤＳツインスター１キロ粒剤',
           'ＳＤＳテラガード２５０グラム', 'ＳＤＳハイカット１キロ粒剤', 'ＳＤＳブルゼータ１キロ粒剤', 'ＳＤＳモーレツ１キロ粒剤',
           'ＳＤＳモーレツフロアブル', 'ＳＤＳ月光１キロ粒剤', 'ＳＤＳ月光フロアブル', 'アールタイプ１キロ粒剤',
           'アールタイプフロアブル', 'アクシズＭＸ１キロ粒剤', 'アグロスクリンチャー１キロ粒剤', 'アグロスシーゼットフロアブル',
           'アシュラ１キロ粒剤', 'アシュラ４００ＦＧ', 'アシュラフロアブル', 'アットウＺ１キロ粒剤', 'アットウＺ４００ＦＧ',
           'アットウＺフロアブル', 'アッパレＺ１キロ粒剤', 'アッパレＺ４００ＦＧ', 'アトトリ１キロ粒剤',
           'アトトリ豆つぶ２５０', 'アネシス１キロ粒剤', 'アバンティ１キロ粒剤', 'アバンティフロアブル',
           'アピログロウＭＸエアー粒剤', 'アルファープロ１キロ粒剤７５', 'アルファープロＨ豆つぶ２５０',
           'アルファープロＬ豆つぶ２５０', 'アワードフロアブル', 'イザナギ１キロ粒剤', 'イザナギフロアブル',
           'イッソウ１キロ粒剤', 'イッテツフロアブル', 'イネキング１キロ粒剤', 'イネキングフロアブル',
           'イネショット１キロ粒剤', 'イネヒーロー１キロ粒剤', 'イネヒーローフロアブル', 'イネリーグ１キロ粒剤',
           'イネリーグフロアブル', 'ウィードコア１キロ粒剤', 'ウィナー１キロ粒剤５１', 'ウィナー１キロ粒剤７５',
           'ウィナーＬフロアブル', 'ウィナーフロアブル', 'ウィニングラン１キロ粒剤', 'ウィニングランフロアブル',
           'ウエスフロアブル', 'ウリホス１キロ粒剤', 'ウルティモＺ１キロ粒剤', 'ウルティモＺフロアブル', 'エリジャンＥＷ乳剤',
           'エンペラー豆つぶ２５０', 'オークスフロアブル', 'オーリック１キロ粒剤', 'オオワザフロアブル',
           'オシオキＭＸ１キロ粒剤', 'オマージュＺ１キロ粒剤', 'オマージュＺフロアブル', 'カイリキＺ１キロ粒剤',
           'カイリキＺフロアブル', 'カウンシルエナジー１キロ粒剤', 'カウンシルエナジーフロアブル',
           'カウンシルコンプリート１キロ粒剤', 'カウンシルコンプリートフロアブル', 'カウントダウン１キロ粒剤',
           'カウントダウンフロアブル', 'カチボシ１キロ粒剤５１', 'カチボシ１キロ粒剤７５', 'カチボシＬフロアブル',
           'カチボシフロアブル', 'カリュード１キロ粒剤', 'カリュードフロアブル', 'ガンガン１キロ粒剤', 'ガンガン豆つぶ２５０',
           'キクンジャーＺ１キロ粒剤', 'キクンジャーＺフロアブル', 'キチットフロアブル', 'キマリテ１キロ粒剤',
           'キマリテフロアブル', 'キラリ１キロ粒剤', 'クサウェポン１キロ粒剤', 'クサウェポンフロアブル',
           'クサトリーＢＳＸ１キロ粒剤５１', 'クサバルカン１キロ粒剤', 'クサバルカンフロアブル', 'クサメッツＬフロアブル',
           'クミスター１キロ粒剤７５', 'クミスターＬ豆つぶ２５０', 'クミスター豆つぶ２５０', 'クラール１キロ粒剤',
           'クラッシュ１キロ粒剤', 'クリンチャー１キロ粒剤', 'クレセント１キロ粒剤７５', 'クレセントフロアブル',
           'クレバールＺ１キロ粒剤', 'クレバールＺフロアブル', 'ゲパード１キロ粒剤', 'ゲパードエアー粒剤',
           'ゴウワン１キロ粒剤５１', 'ゴエモン１キロ粒剤', 'ゴール１キロ粒剤', 'コメット１キロ粒剤', 'コメット顆粒',
           'サスケ粒剤２００', 'サファイア１キロ粒剤', 'サラブレッドＫＡＩ１キロ粒剤', 'サラブレッドＫＡＩ４００ＦＧ',
           'サラブレッドＫＡＩフロアブル', 'サンパンチ１キロ粒剤', 'シアゲＭＦ１キロ粒剤', 'ジェイソウル１キロ粒剤',
           'ジェイソウルフロアブル', 'ジェイフレンド１キロ粒剤', 'ジェイフレンド４００ＦＧ', 'シグナス１キロ粒剤',
           'シグナスエアー粒剤', 'シグナスフロアブル', 'ジャイブスカイ５００グラム粒剤', 'ジャイロ１キロ粒剤',
           'ジャイロフロアブル', 'ジャスタ１キロ粒剤', 'ジャスタフロアブル', 'ジャンダルムＭＸ１キロ粒剤',
           'ジャンダルムＭＸ豆つぶ２５０', 'シュナイデン１キロ粒剤', 'シュナイデンフロアブル', 'ショキニー１キロ粒剤',
           'ショキニー２５０グラム', 'シルトフロアブル', 'シンズイＺ豆つぶ２５０', 'スケダチ１キロ粒剤',
           'スケダチエース１キロ粒剤', 'スマートフロアブル', 'ゼータタイガー１キロ粒剤', 'ゼータタイガー３００ＦＧ',
           'ゼータタイガーフロアブル', 'ゼータハンマー１キロ粒剤', 'ゼータハンマーフロアブル', 'ゼータファイヤ１キロ粒剤',
           'センイチＭＸ１キロ粒剤', 'ダブルスターＳＢ顆粒', 'ダンクショット１キロ粒剤', 'ダンクショット２００粒剤',
           'ダンクショットフロアブル', 'タンボエースＫ\u3000Ｚ１キロ粒剤', 'タンボエーススカイ５００グラム粒剤',
           'タンボパワー１キロ粒剤', 'チャンスタイムＺ１キロ粒剤', 'チャンスタイムＺフロアブル', 'ツイゲキ豆つぶ２５０',
           'ツインスター１キロ粒剤', 'ツルギ１キロ粒剤', 'ツルギ２５０粒剤', 'ツルギフロアブル', 'ディオーレ１キロ粒剤',
           'ディオーレエアー粒剤', 'テイクイット１キロ粒剤', 'テイクイットフロアブル', 'テッケン１キロ粒剤',
           'デルタアタック１キロ粒剤', 'デルタアタック４００ＦＧ', 'デルタアタックフロアブル', 'トクソークサメッツＬフロアブル',
           'トクソーワンベストフロアブル', 'トップガン２５０グラム', 'トップガンＬ２５０グラム', 'トップガンＲ豆つぶ２５０',
           'トドメＭＦ１キロ粒剤', 'ドラゴンホークＺ１キロ粒剤', 'ドラゴンホークＺ３００ＦＧ', 'ドラゴンホークＺフロアブル',
           'ドリフ１キロ粒剤', 'ドンピシャ１キロ粒剤', 'ナギナタ豆つぶ２５０', 'ニトウリュウ１キロ粒剤',
           'ニマイメＺ１キロ粒剤', 'ニマイメＺフロアブル', 'ハイカット１キロ粒剤', 'バイスコープ１キロ粒剤',
           'バサグラン・エアー１キロ粒剤', 'バッチリ１キロ粒剤', 'バッチリ４００ＦＧ', 'バッチリＬＸ１キロ粒剤',
           'バッチリＬＸ４００ＦＧ', 'バッチリＬＸフロアブル', 'パットフルエースＬ２５０グラム', 'パピリカ１キロ粒剤',
           'パピリカフロアブル', 'パンチャー１キロ粒剤', 'ヒエクッパ１キロ粒剤', 'ヒエクッパエース１キロ粒剤',
           'ヒエクリーン１キロ粒剤', 'ヒエクリーン豆つぶ２５０', 'ビクトリーＺ１キロ粒剤', 'ビクトリーＺ４００ＦＧ',
           'ビクトリーＺフロアブル', 'ビッグシュアＺ１キロ粒剤５１', 'ピラクロエース１キロ粒剤', 'ピラクロエースフロアブル',
           'ピラクロン１キロ粒剤', 'ビンワン１キロ粒剤', 'ビンワンフロアブル', 'フォローアップ１キロ粒剤',
           'プライオリティフロアブル', 'プライオリティ豆つぶ２５０', 'フルイニングスカイ５００グラム粒剤',
           'フルスコアＺ１キロ粒剤', 'ブルゼータ１キロ粒剤', 'フルチャージ１キロ粒剤', 'フルチャージスカイ５００グラム粒剤',
           'フルパワーＭＸ１キロ粒剤', 'フルパワーＭＸ５００グラムＦＧ', 'プレキープフロアブル', 'プロヴィジョン１キロ粒剤',
           'ベストコンビスカイ５００グラム粒剤', 'ベストパートナー豆つぶ２５０', 'ベッカク豆つぶ２５０', 'ベルーガ豆つぶ２５０',
           'ベンケイ１キロ粒剤', 'ベンケイ豆つぶ２５０', 'ホクコーエーワン１キロ粒剤', 'ホクコーエーワンフロアブル',
           'ホクコークリンチャー１キロ粒剤', 'ホクコーパンチャー１キロ粒剤', 'ホクコーミスターホームラン１キロ粒剤５１',
           'ホクコーミスターホームランＬフロアブル', 'ホクコーユニハーブフロアブル', 'ホクサンジャスタ１キロ粒剤',
           'ホクサンジャスタフロアブル', 'ホットコンビ２００粒剤', 'ホットコンビフロアブル', 'ボデーガード１キロ粒剤',
           'ボデーガードプロ１キロ粒剤', 'ボデーガードフロアブル', 'ボデーガードプロフロアブル', 'ボデーガード豆つぶ２５０',
           'マキビシＺ１キロ粒剤', 'マスラオ１キロ粒剤', 'マスラオフロアブル', 'ミスターホームラン１キロ粒剤５１',
           'ミスターホームランＬフロアブル', 'ムソウ豆つぶ２５０', 'メガゼータ１キロ粒剤', 'メガゼータ４００ＦＧ',
           'メガゼータフロアブル', 'モーレツ１キロ粒剤', 'モーレツフロアブル', 'モゲトン粒剤', 'ヤイバ１キロ粒剤',
           'ヤイバ豆つぶ２５０', 'ヤブサメ豆つぶ２５０', 'ユニハーブフロアブル', 'ルナクロス１キロ粒剤',
           'レイトリックＺ１キロ粒剤', 'レイトリックＺフロアブル', 'レブラス１キロ粒剤', 'レブラスエアー粒剤',
           'ワイドアタックＤ１キロ粒剤', 'ワイドショット１キロ粒剤', 'ワンステージ１キロ粒剤', '協友シーゼットフロアブル',
           '銀河１キロ粒剤', '月光１キロ粒剤', '月光フロアブル', '石原ワンベストフロアブル', '兆１キロ粒剤',
           '天空１キロ粒剤', '天空エアー粒剤', '天空フロアブル', '東ソーシーゼットフロアブル', '日産イネヒーロー１キロ粒剤',
           '日産クリンチャー１キロ粒剤', '日農イッポン１キロ粒剤７５', '日農イッポンＤ１キロ粒剤５１', '日農イッポンＤフロアブル',
           '日農イッポンフロアブル', '日農クサメッツＬフロアブル', '忍１キロ粒剤', '忍フロアブル', '流星１キロ粒剤',
           '流星エアー粒剤')
        )
        def use_direct():
         use_direct = st.selectbox(
        '使用用途は',
        ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
        )
        if use_direct =="除草剤":
            ine.ine_direct_joso()
        if use_direct =="殺菌剤":
            ine.ine_direct_kin ()
        if use_direct =="殺虫剤":
            ine.ine_direct_insect()
        if use_direct =="殺菌殺虫剤":
            ine.ine_direct_insectkin()
        if use_direct =="農薬肥料":
            ine.ine_direct_felt()
        if use_direct =="植物成長調整剤":
            ine.ine_direct_grow()
def call():
           field = st.slider("今回の散布面積は", min_value = 1, max_value = 10 ,step = 1)
           pest_all = int(field)*4.0
           water = int(field)*3.0
           pest = int(field)*1.0
           return st.subheader(str(field)+"haを散布するということは希釈液="+str(pest_all)+"L 水="+str(water)+"L 農薬="+str(pest)+"L")
###################################################

def mugi_name():
    mugi_name=st.selectbox(
    '今回の作物名は',
    ('麦類','小麦','大麦','麦類(小麦を除く)','麦類(大麦小麦を除く)')
    )
    if mugi_name =="麦類":
        mugi_nomal()
    elif mugi_name =="小麦":
        mugi_small()
    elif mugi_name =="大麦":
        mugi_large()
    elif mugi_name =="麦類(小麦を除く)":
        mugi_except_s()
    elif mugi_name =="麦類(大麦小麦を除く)":
        mugi_except_sandl()
def mugi_nomal():
    mugi_nomal = st.selectbox(
    '使用用途は',
    ('下から選択してください','殺菌剤','殺虫剤')
    )
    if mugi_nomal =="殺菌剤":
        mugi_nomal_kin()
    elif mugi_nomal =="殺虫剤":
        mugi_nomal_insect()
def mugi_small():
    mugi_small=st.selectbox(
    '使用用途は',
    ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
    )
    if mugi_small =="殺菌剤":
        mugi_small_kin()
    elif mugi_small =="殺虫剤":
        mugi_small_insect()
    else:
        st.subheader("現在は殺菌剤と殺虫剤が使用できます")
def mugi_large():
    mugi_large=st.selectbox(
    '使用用途は',
    ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
    )
    if mugi_large =="殺菌剤":
        mugi_large_kin()
    elif mugi_small =="殺虫剤":
        mugi_large_insect()
    else:
        st.subheader("現在は殺菌剤と殺虫剤が使用できます")
def mugi_except_s():
    mugi_except_s=st.selectbox(
    '使用用途は',
    ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
    )
    if mugi_except_s =="殺菌剤":
        mugi_except_s_kin()
    else:
        st.subheader("現在は殺菌剤のみ使用できます")
def mugi_except_sandl():
    mugi_except_sandl =st.selectbox(
    '使用用途は',
    ('下から選択してください','除草剤','殺菌剤','殺虫剤','殺菌殺虫剤','植物成長調整剤','農薬肥料')
    )
    if mugi_except_sandl =="殺虫剤":
        mugi_except_sandl_insect()
    else:
        st.subheader("現在は殺虫剤のみ使用できます")
def mugi_nomal_kin():
    mugi_nomal_kin=st.selectbox(
    "名前は",
    ("ホクコーワークアップＳ乳剤","ワークアップフロアブル")
    )
def mugi_nomal_insect():
    mugi_nomal_insect=st.selectbox(
    "名前は",
    ("アプロードゾル")
    )
def mugi_small_kin():
    mugi_small_kin=st.selectbox(
    "名前は",
    ("クミアイベフトップジンフロアブル","シルバキュアフロアブル","シルベフフロアブル","チルト乳剤２５","トップジンＭゾル","フロンサイドＳＫＹ","ベフトップジンフロアブル","ホクコートップジンＭゾル","ホクサンシルベフフロアブル","ランマンフロアブル","リゾレックスベフランフロアブル","日曹モンカットベフランフロアブル日農ベフトップジンフロアブル",
    "日農モンカットベフランフロアブル")
    )
def mugi_small_insect():
    mugi_small_insect=st.selectbox(
    "名前は",
    ("クミアイスミチオン乳剤","サンケイスミチオン乳剤","トレボンエアー","トレボンスカイＭＣ","ホクコースミチオン乳剤","ホクサンスミチオン乳剤","一農スミチオン乳剤","協友スミチオン乳剤","住化スミチオン乳剤","日産スミチオン乳剤","日農スミチオン乳剤","理研スミチオン乳剤")
    )
def mugi_large_kin():
    mugi_large_kin=st.selectbox(
    "名前は",
    ("チルト乳剤２５","シルバキュアフロアブル")
    )
def mugi_large_insect():
    mugi_large_insect=st.selectbox(
    "名前は",
    ("クミアイスミチオン乳剤","サンケイスミチオン乳剤","ホクコースミチオン乳剤","ホクサンスミチオン乳剤","一農スミチオン乳剤","協友スミチオン乳剤","住化スミチオン乳剤","日産スミチオン乳剤","日農スミチオン乳剤","理研スミチオン乳剤")
    )
def mugi_except_s_kin():
    mugi_except_s_kin=st.selectbox(
    "名前は",
    ("トップジンＭゾル","ホクコートップジンＭゾル")
    )
def mugi_except_sandl_insect():
    mugi_except_sandl_insect=st.selectbox(
    "名前は",
    ("クミアイスミチオン乳剤","サンケイスミチオン乳剤","ホクコースミチオン乳剤","ホクサンスミチオン乳剤","一農スミチオン乳剤","協友スミチオン乳剤","住化スミチオン乳剤","日産スミチオン乳剤","日農スミチオン乳剤","理研スミチオン乳剤")
    )

###########################################################

def hatomugi_kin():
    hatomugi_kin=st.subheader(
    "現在、殺菌剤のロブラール水和剤の一種類のみです")
################################################
def beans_name():
    beans_name=st.selectbox(
    "作物名は",
    ("あずき","だいず")
    )
    if beans_name =="あずき":
        beans_azuki()
    elif beans_name =="だいず":
        beans_soy()
def beans_azuki():
    beans_azuki=st.subheader(
    "現在、殺虫剤のトレボンエアーの一種類のみです"
    )
def beans_soy():
    beans_soy=st.selectbox(
    '使用用途は',
    ('下から選択してください','殺菌剤','殺虫剤','殺菌殺虫剤')
    )
    if beans_soy=="殺菌剤":
        beans_soy_f()
    elif beans_soy =="殺虫剤":
        beans_soy_i()
    elif beans_soy =="殺菌殺虫剤":
        beans_soy_c()
def beans_soy_f():
    beans_soy_f=st.selectbox(
    '名前は',
    ("トップジンＭゾル","ホクコートップジンＭゾル","プランダム乳剤２５","ベルクートフロアブル","アミスター２０フロアブル","ファンタジスタフロアブル","日曹ファンタジスタフロアブル")
    )
def beans_soy_i():
    beans_soy_i=st.selectbox(
    '名前は',
    ('ＭＩＣアディオン乳剤', 'ＭＩＣトルネードエースＤＦ', 'ＭＩＣマトリックフロアブル', 'ＭＲ．ジョーカーＥＷ',
       'ＳＴ3000ＭＲ．ジョーカーＥＷ', 'アディオン乳剤', 'オルトラン水和剤', 'カスケード乳剤',
       'キラップフロアブル', 'クミアイスミチオン乳剤', 'クミアイトルネードエースＤＦ', 'クミアイノーモルト乳剤',
       'サンケイアディオン乳剤', 'サンケイスミチオン乳剤', 'スタークルメイト液剤１０', 'スタークル液剤１０',
       'ダイアジノン粒剤１０', 'ダントツＥＸフロアブル', 'ダントツフロアブル', 'トルネードエースＤＦ', 'トレボンエアー',
       'トレボンスカイＭＣ', 'トレボンスターフロアブル', 'ハスモン天敵', 'プレオフロアブル', 'プレバソンフロアブル５',
       'ペガサスフロアブル', 'ホクコーＭＲ．ジョーカーＥＷ', 'ホクコーアディオン乳剤', 'ホクコーオルトラン水和剤',
       'ホクコーキラップフロアブル', 'ホクコースミチオン乳剤', 'ホクコープレバソンフロアブル５', 'ホクコーロムダンエアー',
       'ホクサンアディオン乳剤', 'ホクサンスミチオン乳剤', 'マトリックフロアブル', 'ランナーフロアブル', 'ロムダンエアー',
       '一農スミチオン乳剤', '丸和トルネードエースＤＦ', '丸和プレバソンフロアブル５', '協友アディオン乳剤',
       '協友スミチオントレボン乳剤', '協友スミチオン乳剤', '協友ダントツフロアブル', '住化スミチオン乳剤',
       '石原アタブロン乳剤', '日産スミチオン乳剤', '日産プレバソンフロアブル５', '日農スミチオン乳剤',
       '日農ノーモルト乳剤', '日農ロムダンエアー', '理研スミチオン乳剤')
    )
def beans_soy_c():
    beans_soy_c=st.selectbox(
    '名前は',
    ("アミスタートレボンＳＥ","シンジェンタアミスタートレボンＳＥ")
    )

###################################################
def corn_name():
    corn_name=st.selectbox(
    "作物名は",
    ("とうもろこし","未成熟とうもろこし")
    )
    if corn_name=="とうもろこし":
        corn_corn()
    if corn_name=="未成熟とうもろこし":
        corn_none()
def corn_corn():
    corn_corn=st.selectbox(
    '殺虫剤のみ使用できます',
    ("アドマイヤーフロアブル","アドマイヤー顆粒水和剤","クミアイアドマイヤーフロアブル","クミアイアドマイヤー顆粒水和剤","ホクサンアドマイヤー顆粒水和剤")
    )
def corn_none():
    corn_none=st.selectbox(
    '使用用途は殺虫剤のみです',
    ("モスピランＳＬ液剤","日農モスピランＳＬ液剤")
    )

###################################################

def suger():
    suger=st.selectbox(
    '使用用途は',
    ("殺虫剤","殺菌剤")
    )
    if suger=="殺虫剤":
        suger_i()
    if suger=="殺菌剤":
        suger_f()
def suger_i():
    suger_i=st.selectbox(
    '名前は',
    ("オルトラン水和剤","トレボンスカイＭＣ","ホクコーオルトラン水和剤")
    )
def suger_f():
    suger_f=st.selectbox(
    '名前は',
    ("グリーンダイセンＭ水和剤","ジマンダイセン水和剤","ホクガード乳剤","ホクコーホクガード乳剤")
    )

###########################################

def potato():
    potato=st.selectbox(
    "作物名は",
    ("ばれいしょ","やまのいも")
    )
    if potato=="ばれいしょ":
        potato_b()
    elif potato=="やまのいも":
        potato_y()
def potato_b():
    potato_b=st.selectbox(
    "使用用途は殺菌剤のみです",
    ("エコメイト","グリーンダイセンＭ水和剤","ザンプロＤＭフロアブル","ジマンダイセン水和剤","バイオキーパー水和剤","プロポーズ顆粒水和剤",
    "ホライズンドライフロアブル","ランマンフロアブル","リライアブルフロアブル","ワイドヒッター顆粒水和剤","日産バイオキーパー水和剤","日産ホライズンドライフロアブル")
    )
def potato_y():
    potato_y=st.selectbox(
    "使用用途は殺菌剤のみです",
    ("トップジンＭゾル","ベルクートフロアブル","ホクコートップジンＭゾル")
    )

#####################################################

def fruit():
    fruit=st.selectbox(
    "作物名は",
    ("かんきつ","かんきつ（ミカンを除く）","みかん")
    )
    if fruit=="かんきつ":
        fruit_cirtus()
    elif fruit=="かんきつ（ミカンを除く）":
        fruit_ex()
    elif fruit=="みかん":
        fruit_orange()
def fruit_cirtus():
    fruit_cirtus=st.selectbox(
    "使用用途は",
    ("殺菌剤","殺虫剤")
    )
    if fruit_cirtus=="殺菌剤":
        fruit_cirtus_f()
    elif fruit_cirtus=="殺虫剤":
        fruit_cirtus_i()
def fruit_cirtus_f():
    fruit_cirtus_f=st.subheader(
    "ナティーボフロアブルのみです"
    )
def fruit_cirtus_i():
    fruit_cirtus_i=st.selectbox(
    "名前は",
    ("アドマイヤーフロアブル","クミアイアドマイヤーフロアブル","モベントフロアブル","アドマイヤープラスフロアブル")
    )
def fruit_ex():
    fruit_ex=st.selectbox(
    "使用できる農薬は殺菌剤のみで名前は",
    ("トップジンＭゾル","ホクコートップジンＭゾル","ジマンダイセン水和剤")
    )
def fruit_orange():
    fruit_orange=st.selectbox(
    "使用用途は",
    ("殺菌剤","殺虫剤")
    )
    if fruit_orange=="殺菌剤":
        fruit_orange_f=st.selectbox(
        "名前は",
        ("ジマンダイセン水和剤","トップジンＭゾル","ベルクートフロアブル","ホクコートップジンＭゾル")
        )
    elif fruit_orange=="殺虫剤":
        fruit_orange_i=st.selectbox(
        "名前は",
        ("クミアイスミチオン乳剤","サンケイスミチオン乳剤","ホクコースミチオン乳剤","一農スミチオン乳剤","協友スミチオン乳剤","住化スミチオン乳剤","日産スミチオン乳剤","日農スミチオン乳剤","理研スミチオン乳剤")
        )

#################################

def cane():
    cane=st.selectbox(
    "殺虫剤のみで名前は",
    ("ＭＩＣサムコルフロアブル１０","サムコルフロアブル１０","サンケイスミチオン乳剤","スタークルメイト液剤１０","スタークル液剤１０","ホクコーサムコルフロアブル１０","一農スミチオン乳剤","丸和サムコルフロアブル１０","兼商サムコルフロアブル１０")
    )

###################################

def tree():
    tree=st.selectbox(
    "作物名は",
    ('まつ（生立木)','すぎ（下刈り）','ヒノキ（下刈り）')
    )
    if tree=="まつ（生立木)":
        tree_i=st.selectbox(
        "殺虫剤のみで名前は",
        ("エコファイターフロアブル３","エコワン３フロアブル","サンケイスミパインＭＣ","サンケイスミパイン乳剤","スミパインＭＣ","マツグリーン液剤２","モリエートＳＣ","モリエートマイクロカプセル","ヤシマスミパインＭＣ","ヤシマスミパイン乳剤","ヤシマモリエートマイクロカプセル","住化スミパイン乳剤")
        )
    if tree=='すぎ（下刈り）':
        tree_s=st.selectbox(
        "除草剤のみで名前は",
        ("ザイトロンフレノック微粒剤","ホドガヤザイトロンフレノック微粒剤")
        )
    if tree=='ヒノキ（下刈り）':
        tree_h=st.selectbox(
        "除草剤のみで名前は",
        ("ザイトロンフレノック微粒剤","ホドガヤザイトロンフレノック微粒剤")
        )

##############################

def veg():
    veg=st.selectbox(
    "作物名は",
    ("アスパラガス","えだまめ","かぼちゃ","かぼちゃ（露地栽培）","キャベツ","くわい","しょうが","せり","だいこん","たまねぎ","にんじん","ブロッコリー","らっきょう","レタス","非結球レタス","れんこん",)
    )
    if veg=="アスパラガス":
        veg_asp=st.selectbox(
        "用途は殺菌剤のみです",
        ("Ｚボルドー","ベルクートフロアブル")
        )
    elif veg=="えだまめ":
        veg_gr=st.selectbox(
        "用途は殺虫剤のみです",
        ("スタークル液剤１０","スタークルメイト液剤１０","ハスモン天敵")
        )
    elif veg=="かぼちゃ":
        veg_pu=st.selectbox(
        "用途は殺菌剤のみです",
        ("ＳＤＳベジセイバー","インプレッション水和剤","セレナーデ水和剤","ベジセイバー")
        )
    elif veg=="かぼちゃ（露地栽培）":
        veg_pu=st.subheader(
        "用途は殺菌剤のサルバトーレＭＥのみです"
        )
    elif veg=="キャベツ":
        veg_c=st.selectbox(
        "用途は殺虫剤のみです",
        ("クミアイノーモルト乳剤","モベントフロアブル","日農ノーモルト乳剤")
        )
    elif veg=="くわい":
        veg_w=st.subheader(
        "用途は除草剤のモゲトン粒剤のみです"
        )
    elif veg=="しょうが":
        veg_j=st.subheader(
        "用途は除草剤のトレボンエアーのみです"
        )
    elif veg=="せり":
        veg_d=st.subheader(
        "用途は除草剤のモゲトン粒剤のみです"
        )
    elif veg=="だいこん":
        veg_r=st.selectbox(
        "用途は殺虫剤のみです",
        ("クミアイノーモルト乳剤","日農ノーモルト乳剤")
        )

    elif veg=="たまねぎ":
        veg_o=st.selectbox(
        "使用用途は",
        ("殺菌剤","殺虫剤")
        )
        if veg_o=="殺菌剤":
            veg_o_f= st.selectbox(
               "名前は",
               ("ザンプロＤＭフロアブル","ジャストフィットフロアブル","トップジンＭゾル","ホクコースミレックス水和剤","ホクコートップジンＭゾル","住化スミレックス水和剤","日農スミレックス水和剤")
               )

        elif veg_o=="殺虫剤":
            veg_o_i=st.selectbox(
        "名前は",
        ("アグロスリン乳剤","オルトラン水和剤","クミアイアグロスリン乳剤","ホクコーオルトラン水和剤","日農アグロスリン乳剤")
        )
    elif veg=="らっきょう":
        veg_s=st.selectbox(
        "用途は殺虫剤のみです",
        ("クミアイスミチオン乳剤","サンケイスミチオン乳剤","スタークルメイト液剤１０","スタークル液剤１０","ホクサンスミチオン乳剤","一農スミチオン乳剤","協友スミチオン乳剤","住化スミチオン乳剤","日産スミチオン乳剤","日農スミチオン乳剤","理研スミチオン乳剤")
        )
    elif veg=="レタス":
        veg_l=st.subheader(
        "用途は殺虫剤のモベントフロアブルのみです"
        )
    elif veg=="れんこん":
        veg_Lo=st.selectbox(
        "用途は殺虫剤のみです",
        ("Ｎスクミンベイト３","ウララ粒剤","オルトラン粒剤","スクミンブルー","スクミンベイト３","ダントツ粒剤","ホクコーオルトラン粒剤","協友ダントツ粒剤")
        )
    elif veg=="非結球レタス":
        veg_n=st.subheader(
        "用途は殺虫剤のモベントフロアブルのみです"
        )

def feed():
    feed=st.subheader(
    "殺菌剤のチルト乳剤２５のみ使用できます"
    )

def grass():
    grass=st.selectbox(
    "作物名は",
    ("日本芝","芝","西洋芝(ブルーグラス)")
    )
    if grass =="日本芝":
        grass_j=st.selectbox(
        "使用用途は植物成長調整剤",
        ("ビオロックフロアブル","プリモマックス液剤","理研ビオロックフロアブル")
        )
    elif grass =="芝":
        grass_t=st.subheader(
        "殺虫剤のシンジェンタアセルプリンのみ使用できます"
        )
    elif grass=="西洋芝(ブルーグラス)":
        grass_w=st.subheader(
        "植物成長調整剤のプリモマックス液剤のみ使用できます"
        )

def other():
    other=st.subheader(
    "東日本大震災により津波被害を受けた農地専用のラウンドアップマックスロードがが使用できます"
    )

####################################################
if crop_class == "稲":
    ine_name()
elif crop_class=='麦類':
    mugi_name()
elif crop_class=="はとむぎ":
    hatomugi_kin()
elif crop_class=="豆類":
    beans_name()
elif crop_class=="とうもろこし":
    corn_name()
elif crop_class=="てんさい":
    suger()
elif crop_class=="芋類":
    potato()
elif crop_class=="果樹類":
    fruit()
elif crop_class=="サトウキビ":
    cane()
elif crop_class=='樹木類':
    tree()
elif crop_class=='野菜類':
    veg()
elif crop_class=="飼料作物":
    feed()
elif crop_class=="芝":
    grass()
elif crop_class=="その他":
    other()

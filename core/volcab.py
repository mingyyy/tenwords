A = "ABUNDANT, ADAPTABLE, ADORABLE, ADORED, ADVENTUROUS, AFFABLE, AFFECTIONATE, AGREEABLE, ALLOWING, ALTRUISTIC, AMAZING, AMBITIOUS, AMIABLE, AMICABLE, AMUSING, ANGELIC, APPRECIATED, APPRECIATIVE, AUTHENTIC, AWARE, AWESOME"
B = "BALANCED, BEAUTIFUL, BELOVED, BEST, BEYOND-FABULOUS, BLESSED, BLISSFUL, BLITHESOME, BOLD, BRAVE, BREATHTAKING, BRIGHT, BRILLIANT, BROAD-MINDED"
C = "CALM, CAPABLE, CAREFUL, CARING, CENTERED, CHAMPION, CHARISMATIC, CHARMING, CHEERFUL, CHERISHED, COMFORTABLE, COMMUNICATIVE, COMPASSIONATE, CONFIDENT, CONSCIENTIOUS, CONSIDERATE, CONTENT, CONVIVIAL, COURAGEOUS, COURTEOUS, CREATIVE, CUTE"
D = "DANDY, DARING, DAZZLED, DECISIVE, DEDICATED, DELICIOUS, DELIGHTFUL, DESIRABLE, DETERMINED, DILIGENT, DIPLOMATIC, DISCREET, DIVINE, DYNAMIC"
E = "EAGER, EASYGOING, EMOTIONAL, EMPATHIC, EMPATHETIC, EMPOWERED, ENCHANTED, ENDLESS, ENERGETIC, ENERGIZED, ENLIGHTENED, ENLIVENED, ENOUGH, ENTHUSIASTIC, ETERNAL, EXCELLENT, EXCITED, EXHILARATED, EXPANDED, EXPANSIVE, EXQUISITE, EXTRAORDINARY, EXUBERANT"
F = "FABULOUS, FAIR-MINDED, FAITHFUL, FANTASTIC, FAVORABLE, FEARLESS, FLOURISHED, FLOWING, FOCUSED, FORCEFUL, FORGIVING, FORTUITOUS, FRANK, FREE, FREE-SPIRITED, FRIENDLY, FULFILLED, FUN, FUN-LOVING, FUNNY"
G = "GENEROUS, GENIAL, GENIUS, GENTLE, GENUINE, GIVING, GLAD, GLORIOUS, GLOWING, GODDESS, GOOD, GOOD HEALTH, GOODNESS, GRACEFUL, GRACIOUS, GRATEFUL, GREAT, GREGARIOUS, GROUNDED"
H = "HAPPY, HAPPY-HEARTED, HARD-WORKING, HARMONIOUS, HEALTHY, HEARTFULL, HEARTWARMING, HEAVEN, HELPFUL, HIGH-SPIRITED, HOLY, HONEST, HOPEFUL, HUMOROUS"
I = "ILLUMINATED, IMAGINATIVE, IMPARTIAL, INCOMPARABLE, INCREDIBLE, INDEPENDENT, INEFFABLE, INNOVATIVE, INSPIRATIONAL, INSPIRED, INTELLECTUAL, INTELLIGENT, INTUITIVE, INVENTIVE, INVIGORATED, INVOLVED, IRRESISTIBLE"
J = "JAZZED, JOLLY, JOVIAL, JOYFUL, JOYOUS, JUBILANT, JUICY, JUST, JUVENESCENT"
K = "KALON, KIND, KIND-HEARTED, KISSABLE, KNOWINGLY, KNOWLEDGEABLE"
L = "LIVELY, LOVABLE, LOVED, LOVELY, LOVING, LOYAL, LUCKY, LUXURIOUS"
M = "MAGICAL, MAGNIFICENT, MARVELOUS, MEMORABLE, MIND-BLOWING, MINDFUL, MIRACLE, MIRACULOUS, MIRTHFUL, MODEST"
N = "NEAT, NICE, NIRVANA, NOBLE, NON-RESISTANT, NOURISHED, NURTURED"
O = "OPEN, OPEN-HEARTED, OPEN-MINDED, OPTIMISTIC, OPULENT, ORIGINAL, OUTSTANDING, OWNING-MY-POWER"
P = "PASSIONATE, PATIENT, PEACEFUL, PERFECT, PERSISTENT, PHILOSOPHICAL, PIONEERING, PLACID, PLAYFUL, PLUCKY, POLITE, POSITIVE, POWERFUL, PRACTICAL, PRECIOUS, PRO-ACTIVE, PROPITIOUS, PROSPEROUS"
Q = "QUICK-WITTED, QUIET"
R = "RADIANT, RATIONAL, READY, RECEPTIVE, REFRESHED, REJUVENATED, RELAXED, RELIABLE, RELIEVED, REMARKABLE, RENEWED, RESERVED, RESILIENT, RESOURCEFUL, RICH, ROMANTIC"
S = "SACRED, SAFE, SATISFIED, SECURED, SELF-ACCEPTING, SELF-CONFIDENT, SELF-DISCIPLINED, SELF-LOVING, SENSATIONAL, SENSIBLE, SENSITIVE, SERENE, SHINING, SHY, SINCERE, SMART, SOCIABLE, SOULFUL, SPECTACULAR, SPLENDID, STELLAR, STRAIGHTFORWARD, STRONG, STUPENDOUS, SUCCESSFUL, SUPER, SUSTAINED, SYMPATHETIC"
T = "THANKFUL, THOUGHTFUL, THRILLED, THRIVING, TIDY, TOUGH, TRANQUIL, TRIUMPHANT, TRUSTING"
U = "ULTIMATE, UNASSUMING, UNBELIEVABLE, UNDERSTANDING, UNF**KWITABLE, UNIQUE, UNLIMITED, UNREAL, UPLIFTED"
V = "VALUABLE, VERSATILE, VIBRANT, VICTORIOUS, VIVACIOUS"
W = "WARM, WARMHEARTED, WEALTHY, WELCOMED, WHOLE, WHOLEHEARTEDLY, WILLING, WISE, WITTY, WONDERFUL, WONDROUS, WORTHY"
X = "XOXO"
Y = "YOUNG-AT-HEART, YOUTHFUL, YUMMY"
Z = "ZAPPY, ZESTFUL, ZING"

word_list_upper = {
             'A': A,
             'B': B,
             'C': C,
             'D': D,
             'E': E,
             'F': F,
             'G': G,
             'H': H,
             'I': I,
             'J': J,
             'K': K,
             'L': L,
             'M': M,
             'N': N,
             'O': O,
             'P': P,
             'Q': Q,
             'R': R,
             'S': S,
             'T': T,
             'U': U,
             'V': V,
             'W': W,
             'X': X,
             'Y': Y,
             'Z': Z}

word_list = {}
for key, value in word_list_upper.items():
    word = value.lower()
    word_list[key] = word

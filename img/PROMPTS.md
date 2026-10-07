# せんせいの いかり 画像プロンプト

Google Flow（旧 ImageFX、https://labs.google/fx/tools/image-fx → flow.google.com）の Nano Banana 2.1 で作成。
先生は 1:1 で face0 を作り、その画像を「編集」で表情だけ変えて face1 → face4 → boom と順につなげると、同じ顔のままになる。
背景は緑（クロマキー）で作り、`python process_images.py` で とうめい PNG にする。

## face0（にこにこ）1:1
Cute Japanese anime-style illustration of a friendly male elementary school teacher in his 30s, bust shot from the chest up, facing the viewer, centered. Short neat black hair with a side part, round black-framed glasses, navy blue suit jacket, white shirt, red necktie. Expression: calm gentle happy smile, eyes curved in a smile, light pink cheeks. Clean thick outlines, bright flat cel shading, kawaii game character art for children. Plain solid flat pure green background (#00FF00 chroma key), no shadows, no gradient. The character's head is in the upper half and the shoulders reach the bottom edge. No text, no letters.

## face1（ん？）編集
Change only the facial expression: a slightly puzzled, wondering look. Eyes open normally with dark pupils, one eyebrow slightly raised, small flat neutral mouth, no pink cheeks. Keep everything else exactly the same: same character, hair, glasses, suit, framing, and the plain flat pure green background.

## face2（イライラ）編集
Change only the facial expression: annoyed and a bit irritated. Eyebrows pulled down and slightly furrowed, eyes narrowed in a stern look, mouth in a small frown, one small cartoon anger vein mark on the forehead. Keep everything else exactly the same: same character, hair, glasses, suit, framing, and the plain flat pure green background.

## face3（おこる）編集
Change only the facial expression: clearly angry and scolding. Eyebrows sharply slanted down in a V shape, glaring eyes, mouth open shouting with teeth showing, face flushed red on the upper half, two red cartoon anger vein marks. Keep everything else exactly the same: same character, hair, glasses, suit, framing, and the plain flat pure green background.

## face4（ばくはつ寸前）編集
Change only the facial expression to furious, about to explode: whole face bright red, both lenses of the glasses glowing solid white so the eyes are hidden, teeth tightly clenched and gritted, trembling lines around the head, white steam puffs blowing out from both sides of the head, three red anger vein marks, a little sweat. Keep everything else exactly the same: same character, hair, glasses frame, suit, framing, and the plain flat pure green background.

## boom（ばくはつ後）編集
Show the same teacher right after a comical cartoon explosion of rage: his hair is blown into a big fluffy black afro, face smudged with grey soot, glasses cracked, mouth wide open yelling furiously, red face, small wisps of dark smoke rising from his head, suit slightly singed. Funny slapstick style for children, not scary, no injuries. Keep the same character design, framing, and the plain flat pure green background.

## bg（教室）16:9
Anime-style background illustration of the front of a Japanese elementary school classroom, seen from the students' seats, 16:9 landscape. A large empty dark green chalkboard fills the upper middle of the wall, wooden frame and chalk tray, a wall clock, small bulletin boards with colorful papers at the sides, windows with afternoon light on the left, a wooden floor. No people, no teacher's desk in the center. Clean thick outlines, bright cel shading, kawaii game art for children, slightly dim warm lighting so characters drawn on top stand out. The chalkboard is completely blank. No text, no letters, no numbers anywhere.

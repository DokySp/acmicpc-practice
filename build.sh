
for item in $*
do
  cp -R ./scaffold $item
  echo "$item 번호 폴더를 생성했습니다."
done

echo "총 $#개의 폴더를 생성했습니다."
echo "즐거운 코딩하세요!!🔥🔥"

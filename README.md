<p align="center">

  <h1> 배틀그라운드_PGC2023 EDA <br><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Trophy.png" alt="Trophy" width="30" height="30" />팀 DANAWA e-sports 은 
PGC2023 GRAND FINAL에서 
어떻게 우승 할 수 있었을까 ?  
 </h1>

<br>

</p>
<a href="https://ibb.co/L9Phj4q"><img src="https://i.ibb.co/nQ08dhV/battleground.png" alt="battleground" border="0"></a>


>본 프로젝트는 배틀그라운드(PUBG, 크래프톤)의 국제 대회, PUBG Global Championship 2023(PGC2023)에서 우승을 차지한 Danawa e-sports팀의 우승 비결을 알아보고자 하였습니다. <br>특히, Grandfinal 매치의 상세한 데이터를 분석하여, Danawa e-sports팀이 어떻게 본 대회에서 승리할 수 있었는지, 그들의 승리에 결정적으로 기여한 요인들을 분석하는 EDA(탐색적 데이터 분석) 프로젝트입니다. 

<br>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20One.png" alt="Keycap Digit One" width="20" height="20" /> Data Introduction

* **`PUBG API`** :  [PUBG API](https://developer.pubg.com/) 

* **`Map images & assets`**:  [GitHub의 PUBG API assets](https://github.com/pubg/api-assets) 

<br>

<h2 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Two.png" alt="Keycap Digit Two" width="20" height="20" /> Language Toools</h2> 
    <div style="margin: ; text-align: left;" "text-align: left;"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" />
    <img src="https://img.shields.io/badge/numpy-4d77cf.svg?style=flat&logo=numpy&logoColor=white" />
    <img src="https://img.shields.io/badge/Matplotlib-11557c.svg?style=flat&logo=Matplotlib&logoColor=white" />
          <img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white"><br>
<br>

</div>

##  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Three.png" alt="Keycap Digit Three" width="20" height="20" /> Data Structure

```js
project_name/
│
├── assets/                # 이미지 파일, 추가적인 자료 파일 등을 저장하는 폴더
│
├── data/                  # 데이터 파일 폴더
│   ├── raw/               # 원본 데이터 파일
│   └── processed/         # 전처리된 데이터 파일
│
├── code/                  # 프로젝트 코드 파일 폴더 
│   ├── exploratory/       # 탐색적 데이터 분석(EDA)
│   └── scripts/           # 데이터 처리,분석 활용 srcipts
│
├── report/                # PPTX,PDF 자료
│
└── README.md              # 프로젝트 README 파일
```
<br>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Four.png" alt="Keycap Digit Four" width="20" height="20" /> Contributor

>**Upstage AI Lab 2기 EDA Project  team6, `HexaHive`입니다!**<br>

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Technologist.png" alt="Technologist" width="25" height="25" />  Members
김도후|유현지|이지환|정소미|
:-:|:-:|:-:|:-:|
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Smiling%20Eyes.png" alt="Smiling Face with Smiling Eyes" width="130" height="110" /></img>|<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Smiling%20Eyes.png" alt="Smiling Face with Smiling Eyes" width="130" height="110" /></img>|<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Smiling%20Eyes.png" alt="Smiling Face with Smiling Eyes" width="130" height="110" /></img>|<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Smiling%20Eyes.png" alt="Smiling Face with Smiling Eyes" width="130" height="110" /></img>
<a href="https://github.com/kimdohoo1102" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/hyeonnjii" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/jihwan1229" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/sommizzu" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>

# CIFAR-10-C Dataset Analysis

현재 저장된 `CIFAR-10-C` 데이터셋(`C:\Users\a3426\data\corruption\CIFAR-10-C`)에 대한 상세 구조 분석 내용입니다. 

> [!NOTE]
> 이 데이터셋은 원본 CIFAR-10 테스트 데이터셋(10,000장)에 대해 각 손상(Corruption) 별로 5단계의 강도(Severity)를 적용한 평가용 벤치마크 데이터입니다.

## 1. 파일 구성 요약
- **총 파일 개수**: `20개`
- **파일 형식**: 모두 Numpy 배열 바이너리 파일 (`.npy`)
- **구분**: 정답 라벨 파일 1개(`labels.npy`) + 이미지 파일 19개(`gaussian_noise.npy` 등 손상 종류별 1개씩)

## 2. 이미지 데이터(Feature) 분석
손상 유형에 따른 각 파일(예: `gaussian_noise.npy`)의 내부 구조입니다.

| 항목 | 수치 / 정보 | 설명 |
|---|---|---|
| **Shape (형태)** | `(50000, 32, 32, 3)` | 50,000장의 이미지. 각 이미지는 가로 32, 세로 32, 3개의 색상 채널(RGB)로 구성됨 |
| **Data Type (타입)** | `uint8` | 각 픽셀 값이 0~255 사이의 정수 포맷 |
| **강도(Severity)** | 5단계 | 처음 1만장은 강도 1, 다음 1만장은 강도 2... 마지막 1만장은 강도 5의 규칙을 가짐 |

## 3. 정답 데이터(Label) 분석
이미지에 매칭되는 클래스 정답 파일(`labels.npy`)의 내부 구조입니다.

| 항목 | 수치 / 정보 | 설명 |
|---|---|---|
| **Shape (형태)** | `(50000,)` | 각 이미지에 대응되는 50,000개의 1차원 정답 배열 |
| **Data Type (타입)** | `uint8` | 0~9 사이의 정수 클래스 번호 |

### 클래스별 분포(Distribution)
총 10가지(0~9)의 클래스가 완벽하게 동일한 비율로 구성되어 있습니다.
- 0 ~ 9 각 클래스당 **정확히 5,000개**씩 존재
- (클래스당 1,000장의 원본 이미지가 5단계의 손상 강도로 각각 변환되었기 때문에 5,000개가 됩니다.)

## 4. 지원되는 손상 환경 (Corruptions)
테스트 코드에 정의된 `gaussian_noise`, `shot_noise`, `impulse_noise`, `defocus_blur`, `glass_blur`, `motion_blur`, `zoom_blur`, `snow`, `frost`, `fog`, `brightness`, `contrast`, `elastic_transform`, `pixelate`, `jpeg_compression` 등의 파일이 모두 153MB 용량으로 정확히 준비되어 있습니다.

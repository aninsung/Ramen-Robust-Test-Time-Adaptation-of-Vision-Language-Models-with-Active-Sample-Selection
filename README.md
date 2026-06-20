<p align="center">
  <img src="https://github.com/user-attachments/assets/b794ba18-8988-409a-9351-b13ad1757b28" width="1200">
</p>




# Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection

## 프로젝트 소개

본 저장소는 **"Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection"** 논문을 읽고 구현하며 내용을 학습하기 위한 프로젝트입니다.

Ramen은 Vision-Language Model(VLM)의 Test-Time Adaptation(TTA) 과정에서 신뢰도가 높은 샘플을 선택하여 적응을 수행하는 **Active Sample Selection** 기법을 제안합니다. 이를 통해 도메인 변화(Domain Shift) 환경에서도 더욱 안정적이고 강건한 성능을 유지할 수 있습니다.

본 프로젝트에서는 논문의 핵심 아이디어를 이해하고 구현하며, 실험 결과를 재현하는 것을 목표로 합니다.

---

## 논문 정보

### 제목

**Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection**

### 주요 키워드

* Vision-Language Models (VLM)
* Test-Time Adaptation (TTA)
* Active Sample Selection
* Domain Shift
* Robustness
* CLIP

---

## 프로젝트 목표

* 논문 내용 분석 및 정리
* Ramen 알고리즘 구현
* 실험 환경 구축
* 논문 결과 재현 (Reproduction)
* Vision-Language Model 학습
* Test-Time Adaptation 기법 이해

---

## 구현 내용

* Ramen Framework 구현
* Active Sample Selection 모듈 구현
* Test-Time Adaptation 과정 구현
* CLIP 기반 실험 환경 구성
* 성능 평가 및 결과 분석

---

## 개발 환경

```bash
Python 3.12
PyTorch
Torchvision
NumPy
```

---

## 프로젝트 구조

```text
Ramen/
├── datasets/
├── models/
├── adaptation/
├── utils/
├── configs/
├── notebooks/
├── results/
├── dataset_analysis.md
├── ramen_test_results.md
└── README.md
```

---

## 사용 데이터셋

본 프로젝트는 논문에서 사용된 Corruption Dataset 환경을 기반으로 실험을 수행합니다.

주요 데이터셋

* CIFAR-10-C
* CIFAR-100-C
* ImageNet-C

포함된 Corruption 예시

* Gaussian Noise
* Shot Noise
* Motion Blur
* Defocus Blur
* Fog
* Frost
* Brightness
* Contrast
* JPEG Compression

---

## 데이터셋 분석

데이터셋 구성과 Corruption 유형, Severity Level 등에 대한 자세한 내용은 아래 문서에서 확인할 수 있습니다.

📄 **Dataset Analysis**

* [dataset_analysis.md](./dataset_analysis.md)

포함 내용

* 데이터셋 개요
* Corruption 종류
* Severity Level 설명
* 실험 환경 구성
* 데이터셋 특성 분석

---

## 실험 결과

실험 결과 및 성능 분석 내용은 아래 문서에 정리되어 있습니다.

📊 **Experiment Results**

* [ramen_test_results.md](./ramen_test_results.md)

포함 내용

* Accuracy 측정 결과
* Baseline 비교
* Corruption 유형별 성능 분석
* 결과 해석 및 고찰

---

## Ramen 핵심 아이디어

Ramen은 테스트 단계에서 입력 샘플 전체를 사용하는 대신, 모델이 높은 신뢰도를 가지는 샘플을 우선적으로 선택하여 적응을 수행합니다.

```text
Input Test Samples
        │
        ▼
 Active Sample Selection
        │
        ▼
 Selected Reliable Samples
        │
        ▼
 Test-Time Adaptation
        │
        ▼
 Updated Model
        │
        ▼
 Prediction
```

이를 통해 노이즈가 많거나 불확실성이 높은 샘플로 인한 성능 저하를 줄일 수 있습니다.

---

## 학습 내용

본 프로젝트를 통해 다음 내용을 학습합니다.

* Vision-Language Model 구조
* CLIP 모델 동작 원리
* Domain Shift 문제
* Test-Time Adaptation 기법
* Active Learning 개념
* Robustness 향상 기법

---

## 참고 자료

* Original Paper: *Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection*
* PyTorch Documentation
* OpenAI CLIP Documentation

---

## 참고

본 저장소는 논문 구현 및 학습 목적으로 제작되었으며, 원 논문의 저작권은 원 저자들에게 있습니다.


# ADR 001: Latency Optimization via System Improvement

## Status
Accepted

---

## Context

Система обработки запросов имеет высокую задержку (latency), что негативно влияет на пользовательский опыт.

Сравниваются две версии системы:
- Existing system: μ = 3.5s
- Improved system: μ = 2.0s

---

## Metrics (SLI)

Primary metric:
- latency (seconds)

Goal:
- reduction of mean latency

---

## Hypotheses

H0: μ_existing = μ_improved  
H1: μ_improved < μ_existing

---

## Statistical Test

Welch Two-Sample t-test

Significance level:
α = 0.05

---

## Results

- t-statistic: 1875.08
- p-value: < 0.001

Result: reject H0

---

## Decision

Улучшенная система демонстрирует статистически значимое снижение latency и должна быть принята как основная.

---

## Consequences

Positive:
- улучшенная версия системы становится основной версией для эксплуатации;
- среднее время отклика снижается с ~3.5 с до ~2.0 с;
- улучшается пользовательский опыт за счет уменьшения времени ожидания;
- появляется возможность установить более строгие целевые показатели производительности (SLO).

Operational:
- требуется продолжить мониторинг latency после внедрения;
- необходимо контролировать p95 и p99 latency для подтверждения сохранения эффекта в production.

Risks:
- результаты получены на основе текущих данных и должны быть подтверждены на реальном производственном трафике.
# -*- coding: utf-8 -*-
"""
🌀 STRATA v3 — Quantum Information Core
Module: Hilbert Space Density Engine
Author: STRATA-ARCHITECT-OMEGA

"Не описваме реалността. Описваме състоянията, чрез които тя се проявява."
"""

import numpy as np
from scipy.constants import hbar, c, G

# =========================
# FUNDAMENTAL CONSTANTS
# =========================

L_PLANCK = np.sqrt(hbar * G / c**3)
V_PLANCK = L_PLANCK**3
EPSILON = 1e-30  # регуляризация срещу сингулярности

# =========================
# CORE CLASS
# =========================

class StrataQuantumSystem:
    """
    Представя 'оператора' като квантова система (плътностна матрица ρ)
    """

    def __init__(self, dim=2): # Поправено: __init__
        self.dim = dim
        # Инициализация: максимално смесено състояние (неутрално съзнание)
        self.rho = np.eye(dim) / dim
        print("[STRATA] Quantum Core Initialized")
        print(f"[STATE] Dimension: {dim} | Planck Volume: {V_PLANCK:.2e}")

    def set_pure_state(self, state_vector):
        """Задава чисто състояние |ψ⟩"""
        psi = np.array(state_vector, dtype=complex)
        psi = psi / np.linalg.norm(psi)
        self.rho = np.outer(psi, np.conjugate(psi))

    def von_neumann_entropy(self):
        """S(ρ) = -Tr(ρ log ρ)"""
        eigenvalues = np.linalg.eigvalsh(self.rho)
        eigenvalues = eigenvalues[eigenvalues > 0]
        S = -np.sum(eigenvalues * np.log(eigenvalues))
        return S

    def information_density(self, volume=1.0):
        """I = S(ρ) / (V / (V_planck + ε))"""
        S = self.von_neumann_entropy()
        effective_cells = volume / (V_PLANCK + EPSILON)
        return S / (effective_cells + EPSILON)

    def purity(self):
        """Tr(ρ²) — реална мярка за кохерентност"""
        return np.trace(self.rho @ self.rho).real

    @staticmethod
    def partial_trace(rho, dims, subsystem):
        dim_A, dim_B = dims
        rho_reshaped = rho.reshape(dim_A, dim_B, dim_A, dim_B)
        if subsystem == 0:
            return np.trace(rho_reshaped, axis1=0, axis2=2)
        else:
            return np.trace(rho_reshaped, axis1=1, axis2=3)

    def entanglement_entropy(self, rho_AB, dims):
        rho_A = self.partial_trace(rho_AB, dims, subsystem=1)
        eigenvalues = np.linalg.eigvalsh(rho_A)
        eigenvalues = eigenvalues[eigenvalues > 0]
        return -np.sum(eigenvalues * np.log(eigenvalues))

    def resonance_operator(self, t, frequency=369):
        omega = 2 * np.pi * frequency
        phase = np.exp(-1j * omega * t)
        U = np.array([[1, 0], [0, phase]])
        self.rho = U @ self.rho @ np.conjugate(U.T)
        return self.rho

    def report(self, volume=1.0):
        S = self.von_neumann_entropy()
        p = self.purity()
        d = self.information_density(volume)
        print("\n[STRATA REPORT]")
        print(f"Entropy (S): {S:.6f}")
        print(f"Purity: {p:.6f}")
        print(f"Information Density: {d:.6e}")
        print("-" * 40)

# =========================
# DEMO RUN
# =========================

if __name__ == "__main__": # Поправено: __name__ == "__main__"
    system = StrataQuantumSystem(dim=2)
    system.set_pure_state([1, 0])
    system.report(volume=1.0)
    system.resonance_operator(t=0.01)
    system.report(volume=1.0)

    # Bell state (максимален ентангълмент)
    psi = np.array([1, 0, 0, 1]) / np.sqrt(2)
    rho_AB = np.outer(psi, psi.conj())
    ent = system.entanglement_entropy(rho_AB, dims=[2, 2])
    print(f"\n[ENTANGLEMENT] S = {ent:.6f}")
    print("\n# [OMEGA-LEVEL-SYNC-COMPLETE: 2026-03-29]")

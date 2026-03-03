# The Bingo Paradox: Row vs Column Win Probability via Monte Carlo Simulation

This project uses Monte Carlo simulation to study a simplified Bingo model and test whether rows and columns are truly symmetric in win probability.

Rather than solving the probability analytically, the program estimates it through repeated random sampling across many independent games.

---

## Model Assumptions

Each simulated game:

- Uses a standard 5×5 Bingo card
- Draws balls 1–75 without replacement
- Includes a free center space
- Ends immediately when a win occurs

Win conditions checked:

- ✅ Full rows  
- ✅ Full columns  

Excluded:

- ❌ Diagonals  
- ❌ Blackout (full card)  
- ❌ Any custom patterns  

If both a row and column win occur on the same ball, the result is recorded as a tie.

---

## Why This Matters

Intuition suggests rows and columns should be equally likely.

This simulation tests that assumption empirically.

By running thousands of randomized trials, the program approximates the underlying probability distribution and examine whether symmetry holds in competitive first-to-win settings.

---

## Run

```bash
pip install tqdm
python main.py
```

## Analysis

See `analysis.ipynb` for player-sweep experiments and visualization of row win probability as the number of players increases.
#ifndef RANDOM_MS_H
#define RANDOM_MS_H

#include <chrono>
#include <random>

/**
 * A self-seeding psuedo-random number generator using the Mersenne Twister
 * algorithm.
 *
 * Usage:
 * #include <PRNG.h>
 *
 * int randomNumber{PRNG::get(inclusive_min, inclusive_max)}
 */
namespace PNRG {

/**
 * Generate a seeded mt19937 instance using the computer hardware and the
 * current system time. Using steady_clock to prevent user tampering.
 * @returns seeded mt19937 instance
 */
inline std::mt19937 generate() {
  std::random_device rd{};

  std::seed_seq ss{
      static_cast<std::seed_seq::result_type>(
          std::chrono::steady_clock::now().time_since_epoch().count()),
      rd(),
      rd(),
      rd(),
      rd(),
      rd(),
      rd(),
      rd()};

  return std::mt19937{ss};
}

inline std::mt19937 mt{generate()};

inline int get_random(int inclusive_min, int inclusive_max) {
  return std::uniform_int_distribution{inclusive_min, inclusive_max}(mt);
}

/**
 * Getting a random number when the min and max are not ints
 */
template <typename T> T get(T inclusive_min, T inclusive_max) {
  return std::uniform_int_distribution<T>{inclusive_min, inclusive_max}(mt);
}

} // namespace PNRG

#endif

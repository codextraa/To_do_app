import nextPlugin from '@next/eslint-plugin-next';
import js from '@eslint/js';

export default [
  js.configs.recommended, // Standard JavaScript rules
  {
    files: ['**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx'],
    plugins: {
      '@next/next': nextPlugin,
    },
    rules: {
      ...nextPlugin.configs.recommended.rules, // Next.js recommended rules
      'no-unused-vars': 'warn', // Custom rule for unused variables
    },
    languageOptions: {
      parserOptions: {
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
  },
];

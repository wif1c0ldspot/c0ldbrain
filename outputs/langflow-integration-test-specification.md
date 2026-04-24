---
title: "Langflow Integration Test Specification"
type: specification
status: draft
summary: "Comprehensive test specifications for Langflow Claude Code integration components"
---

# Test Specification: Langflow Claude Code Integration

**Scope:** All custom components for Langflow implementation  
**Framework:** pytest + Langflow test utilities  
**Coverage Target:** 90% line coverage, 100% critical path coverage

---

## 1. Test Categories

### 1.1 Unit Tests
Test components in isolation with mocked dependencies.

### 1.2 Integration Tests
Test components with real dependencies (test LLM, test tools).

### 1.3 End-to-End Tests
Test complete flows through Langflow canvas.

### 1.4 Performance Tests
Measure latency, throughput, memory usage.

### 1.5 Chaos Tests
Inject errors to verify recovery mechanisms.

---

## 2. Component Test Specifications

### 2.1 StreamingAgentLoop

#### Unit Tests
```python
def test_streaming_yields_tokens():
    """TC-SAL-001: Stream yields tokens in real-time"""
    # Given: Mock LLM that generates tokens slowly
    # When: Run StreamingAgentLoop
    # Then: Tokens yielded before generation completes
    
def test_cancellation_stops_execution():
    """TC-SAL-002: Cancellation stops execution cleanly"""
    # Given: Running agent loop
    # When: Cancel called
    # Then: Loop stops, cleanup runs, no exceptions
    
def test_five_phases_execute_in_order():
    """TC-SAL-003: 5 phases execute in correct order"""
    # Given: Mocked dependencies for each phase
    # When: Run single turn
    # Then: Setup → Model → Recovery → Tools → Decision
    
def test_backpressure_pauses_generation():
    """TC-SAL-004: Backpressure pauses generation"""
    # Given: Slow consumer
    # When: Fast generator
    # Then: Generator pauses when consumer stops pulling
    
def test_error_recovery_triggers():
    """TC-SAL-005: Error recovery triggers correctly"""
    # Given: Model returns recoverable error
    # When: Recovery phase executes
    # Then: Retry with adjusted parameters
```

#### Integration Tests
```python
def test_full_conversation_10_turns():
    """IT-SAL-001: 10-turn conversation completes"""
    # Setup: Real LLM, mock tools
    # Execute: 10 turns with tool calls
    # Verify: All turns complete, context maintained
    
def test_context_window_management():
    """IT-SAL-002: Context window managed across long conversation"""
    # Setup: Conversation that exceeds token limit
    # Execute: Run until compaction triggers
    # Verify: Compaction runs, conversation continues
```

#### Performance Tests
```python
def test_latency_overhead():
    """PT-SAL-001: Overhead <50ms per turn"""
    # Setup: Measure baseline LLM latency
    # Execute: 100 turns with component
    # Verify: Median overhead <50ms
    
def test_memory_bounded():
    """PT-SAL-002: Memory usage bounded"""
    # Setup: Monitor memory during 1000-turn conversation
    # Verify: Memory growth <10MB after initial setup
```

#### Chaos Tests
```python
def test_rate_limit_recovery():
    """CT-SAL-001: Recovers from rate limits"""
    # Inject: 429 errors at 50% rate
    # Verify: Component retries with backoff, eventually succeeds
    
def test_context_overflow_recovery():
    """CT-SAL-002: Recovers from context overflow"""
    # Inject: prompt-too-long errors
    # Verify: Compaction triggers, retry succeeds
```

---

### 2.2 ToolConcurrencyClassifier

#### Unit Tests
```python
def test_read_tools_classified_parallel():
    """TC-TCC-001: Read tools marked for parallel execution"""
    # Given: List of read tools
    # When: Classify
    # Then: All in parallel bucket
    
def test_write_tools_classified_serial():
    """TC-TCC-002: Write tools marked for serial execution"""
    # Given: List of write tools
    # When: Classify
    # Then: All in serial bucket
    
def test_mixed_batch_partitioned():
    """TC-TCC-003: Mixed batch correctly partitioned"""
    # Given: Mixed read/write tools
    # When: Classify
    # Then: Read in parallel, write in serial
```

#### Integration Tests
```python
def test_10_parallel_reads():
    """IT-TCC-001: 10 read tools execute in parallel"""
    # Setup: 10 read tool calls
    # Execute: Classify and execute
    # Verify: All complete in <2x single tool time
    
def test_serial_writes_no_race():
    """IT-TCC-002: Serial writes prevent race conditions"""
    # Setup: 5 write tools targeting same file
    # Execute: Classify and execute
    # Verify: No corruption, all writes atomic
```

---

### 2.3 ContextCompactor

#### Unit Tests
```python
def test_microcompact_caches_unchanged():
    """TC-CC-001: Microcompact caches unchanged tool results"""
    # Given: Tool result unchanged from previous turn
    # When: Microcompact runs
    # Then: Result replaced with cached reference
    
def test_snip_preserves_protected_tail():
    """TC-CC-002: Snip preserves protected tail"""
    # Given: 100 messages, protected_tail=10
    # When: Snip compact runs
    # Then: Last 10 messages unchanged, first 90 removed
    
def test_auto_compact_summarizes():
    """TC-CC-003: Auto compact produces coherent summary"""
    # Given: 50 messages requiring summarization
    # When: Auto compact runs
    # Then: Summary captures key information
```

#### Performance Tests
```python
def test_microcompact_near_zero_cost():
    """PT-CC-001: Microcompact <1ms overhead"""
    # Execute: 1000 microcompactions
    # Verify: Median <1ms
    
def test_collapse_handles_1000_turns():
    """PT-CC-002: Collapse handles 1000-turn sessions"""
    # Setup: 1000-turn conversation
    # Execute: Full compaction
    # Verify: Completes in <30s, context valid
```

---

### 2.4 ErrorRecoveryPipeline

#### Unit Tests
```python
def test_429_respects_retry_after():
    """TC-ERP-001: 429 recovery respects Retry-After"""
    # Given: 429 with Retry-After: 5
    # When: Recovery runs
    # Then: Waits 5s, retries
    
def test_529_triggers_model_fallback():
    """TC-ERP-002: 3x 529 triggers model fallback"""
    # Given: 3 consecutive 529 errors
    # When: Recovery runs
    # Then: Switches to fallback model
    
def test_backoff_formula_correct():
    """TC-ERP-003: Backoff formula matches spec"""
    # Given: Attempt counts 1-10
    # When: Calculate delays
    # Then: Match: min(500ms × 2^attempt, 32s) + random(0, 0.25 × baseDelay)
```

#### Chaos Tests
```python
def test_random_errors_recover():
    """CT-ERP-001: Recovers from random error injection"""
    # Inject: Random mix of 429, 529, network errors
    # Verify: Eventually succeeds or graceful failure
```

---

## 3. End-to-End Flow Tests

### 3.1 Basic Agent Flow
```python
def test_e2e_simple_coding_task():
    """E2E-001: Complete simple coding task"""
    # Flow: User request → AgentLoop → Tool calls → Response
    # Verify: Task completed, correct code generated
    
def test_e2e_multi_turn_debugging():
    """E2E-002: Multi-turn debugging session"""
    # Flow: Bug report → Investigation → Fix → Verify
    # Verify: Bug fixed, tests pass
```

### 3.2 Error Recovery Flow
```python
def test_e2e_rate_limit_recovery():
    """E2E-003: Recovers from rate limits mid-task"""
    # Inject: Rate limit during long task
    # Verify: Recovers, completes task
    
def test_e2e_context_overflow_handling():
    """E2E-004: Handles context overflow gracefully"""
    # Trigger: Very long conversation
    # Verify: Compaction runs, conversation continues
```

### 3.3 Multi-Agent Flow
```python
def test_e2e_parallel_subagents():
    """E2E-005: Parallel sub-agents on same repo"""
    # Flow: Parent spawns 3 sub-agents
    # Verify: All complete, no conflicts, changes merge
```

---

## 4. Test Data Fixtures

### 4.1 Conversation Fixtures
```yaml
# fixtures/conversations/short.yaml
messages:
  - role: user
    content: "Hello"
  - role: assistant
    content: "Hi there!"
    
# fixtures/conversations/long.yaml  
messages:
  # 1000 messages for compaction testing
```

### 4.2 Tool Call Fixtures
```yaml
# fixtures/tools/mixed_batch.yaml
tool_calls:
  - tool: read
    args: {file: "src/main.py"}
  - tool: grep
    args: {pattern: "TODO", path: "."}
  - tool: edit
    args: {file: "src/main.py", new_content: "..."}
```

### 4.3 Error Fixtures
```yaml
# fixtures/errors/rate_limit.yaml
error:
  type: 429
  headers:
    Retry-After: 5
  message: "Rate limit exceeded"
```

---

## 5. Test Execution

### 5.1 Local Development
```bash
# Run unit tests
pytest tests/unit/ -v

# Run integration tests
pytest tests/integration/ -v

# Run with coverage
pytest --cov=langflow_claude --cov-report=html

# Run specific component
pytest tests/unit/test_streaming_agent_loop.py -v
```

### 5.2 CI/CD
```yaml
# .github/workflows/test.yml
- name: Run tests
  run: |
    pytest tests/unit/ --cov --cov-fail-under=90
    pytest tests/integration/
    pytest tests/e2e/ --timeout=300
```

---

## 6. Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Line Coverage | ≥90% | pytest-cov |
| Branch Coverage | ≥80% | pytest-cov |
| Critical Path | 100% | Manual verification |
| Unit Test Count | ≥50 | Test count |
| Integration Test Count | ≥20 | Test count |
| E2E Test Count | ≥10 | Test count |
| Test Execution Time | <5 min | CI timing |
| Flaky Tests | 0% | CI history |

---

## 7. Maintenance

### Adding New Tests
1. Identify component and test category
2. Use naming convention: `{category}-{component_id}-{sequence}`
3. Follow Given-When-Then structure
4. Update this specification
5. Run full suite before commit

### Test Review Checklist
- [ ] Test has clear purpose and name
- [ ] Test follows Given-When-Then structure
- [ ] Test is deterministic (no randomness without seed)
- [ ] Test cleans up resources
- [ ] Test runs in <10 seconds (unit) / <60 seconds (integration)
- [ ] Test has appropriate fixtures
- [ ] Test covers both success and failure cases

---

*This specification evolves with implementation. Update as components are added or requirements change.*

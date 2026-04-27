# Memory in Claude Managed Agents
# Source: https://x.com/rlancemartin/status/2047720067107033525
# Author: Lance Martin (@RLanceMartin)
# Date: 2026-04-24
# Engagement: 368 likes, 49 retweets, 115,559 views, 855 bookmarks
# Retrieved: 2026-04-27 via fxtwitter API

---

Claude Managed Agents (available on the Claude Platform) now has memory. Memories are stored as files and are accessible across sessions, allowing the agent to learn from experience. Memories can also be exported via the API.

@DavidSHershey shared a story about agent memory with me: in his work on Claude Plays Pokémon, he gave Claude a tool to read and write memory files to a folder. These memory files were meant to help Claude navigate the game.

This didn't work very well with earlier models. Sonnet 3.5 treated memory as a transcript, writing down what non-player characters said rather than what mattered. After 14,000 steps it had 31 memory files, but had not made much progress (it was stuck in the second town).

To overcome these limitations, many papers have proposed harnesses with tooling to manage memory. @tedsumers CoALA paper and the memGPT work from @sarahwooders and @charlespacker are two of my favorites. These use ideas from cognitive sciences and operating system to model agent memory.

But the Pokémon work showed an interesting result: later models learned to use the filesystem to organize memory much better. Opus 4.6, at the same step count, had 10 files organized into directories, three gym badges, and a learnings file distilled from its own failures.

This example highlights a trend: give Claude general tools to manage its own context and actions. Claude can learn to use general tools to solve problems, like memory, with scaling intelligence.

With a general tool to manage files, we've seen Claude learn what to save and how to organize its own memories. @Letta_AI independently showed that a filesystem can outperform specialized memory tools.

This story explains why we use the filesystem for memory in Claude Managed Agents. Files can be organized however Claude wants, using its standard file tools. The platform just persists files between sessions using memory stores, which are workspace-scoped collections of text documents that outlive any single session.

When you attach a memory store to a session, it's mounted into the container as a directory at /mnt/memory/<store-name>/. A short note about the mount is automatically injected into the system prompt so Claude knows it's there.

Multiple agents can access the same memory store and the platform will sync memories in real time: if one agent makes an edit, that edit will be reflected in the filesystem of all other agents that have the memory store mounted. It also will handle concurrency to make sure one agent doesn't overwrite the memory updates made by another agent.

Files have an additional benefit - they are interpretable and sharable. In the Pokémon example, @DavidSHershey was able to just download and share the memory folders. With Managed Agents you can also export memories.

This sets up a simple way to think about context in Managed Agents: there is a session log and a memory store. Claude can fetch and transform session context over the course of a task. The session lives outside the context window. Claude can write files to the memory store if it wants to persist context across sessions.

References:
- CoALA paper (@tedsumers)
- memGPT (@sarahwooders, @charlespacker)
- Claude Plays Pokémon (@DavidSHershey)
- Letta AI filesystem vs specialized memory tools

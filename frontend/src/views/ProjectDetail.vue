<template>
  <!-- If project is not found -->
  <div v-if="!projectInfo.value == {}">
    <h2>Project not found</h2>
  </div>

  <!-- If project IS found -->
  <div v-else class="project-detail">
    <div class="project-media">
      <button class="return-btn" @click="goBack">
        Return
      </button>

      <h1 class="project-title">{{ projectInfo.title }}</h1>
        
      <div class="project-preview-wrapper">
        <!-- v-if handles the check for undefined or empty strings -->
        <video
          v-if="projectInfo.video"
          ref="videoRef"
          :src="projectInfo.video"
          autoplay
          loop
          muted
          playsinline
          controls
          @loadedmetadata="onVideoReady"
        ></video>
        <img
          v-else-if="projectInfo.image"
          :src="projectInfo.image"
          :alt="projectInfo.title"
        />
      </div>

      <div class="project-meta">
        <span class="project-date">{{ projectInfo.date }}</span>
        <span class="project-status">Status: {{ projectInfo.status }}</span>
        <div class="project-tech">
            <div v-if="projectInfo.skills && projectInfo.skills.length" class="skills_stack">
              <span
                v-for="skill in projectInfo.skills"
                :key="skill.id || skill.name"
                class="tech-badge"
              >
                {{ skill.name }}
              </span>
            </div>

            <div v-if="projectInfo.techs && projectInfo.techs.length" class="techs_stack">
              <span
                v-for="tech in projectInfo.techs"
                :key="tech.id || tech.name"
                class="tech-chip"
              >
                {{ tech.name }}
              </span>
            </div>
        </div>
      </div>
    </div>

    <div class="project-info">
      <div class="project-short-desc">
        <div class="detail-title">
          <h1>Project overview</h1>
        </div>

        <p class="lead" v-if="projectInfo.shortDesc">{{ projectInfo.shortDesc }}</p>
      </div>

      <div class="info-layout">
        <nav v-if="infoBlocks.some((block) => block.title)" class="content-nav" aria-label="Project details">
          <h2 class="content-nav-title">Contents</h2>
          <ol class="content-nav-list">
            <template v-for="(block, index) in infoBlocks" :key="`nav-${block.id || index}`">
              <li v-if="block.title">
                <a :href="`#detail-section-${index}`">{{ block.title }}</a>
              </li>
            </template>
          </ol>
        </nav>

        <div class="info-blocks">
          <!-- One block per row in projectInfo.details, alternating media side -->
          <article
            v-for="(block, index) in infoBlocks"
            :id="`detail-section-${index}`"
            :key="block.id || index"
            class="info-block"
            :class="{ 'has-media': block.hasMedia, flip: block.flip }"
          >
            <div class="info-text">
              <h3 v-if="block.title">{{ block.title }}</h3>
              <p>{{ block.info }}</p>
            </div>

            <div
              v-if="block.hasMedia"
              class="info-media"
              role="button"
              tabindex="0"
              :aria-label="`Expand ${block.title || 'project media'}`"
              @click="openMedia(block)"
              @keydown.enter.prevent="openMedia(block)"
              @keydown.space.prevent="openMedia(block)"
            >
              <video
                v-if="block.type === 'video'"
                :src="block.url"
                controls
                playsinline
                preload="metadata"
              ></video>
              <img
                v-else
                :src="block.url"
                :alt="block.title || projectInfo.title"
                loading="lazy"
              />
            </div>
          </article>

          <p v-if="infoBlocks.length === 0" class="no-details">
            No detailed information available for this project yet.
          </p>
        </div>
      </div>

      <transition name="modal-fade">
        <div
          v-if="expandedMedia"
          class="media-modal"
          role="dialog"
          aria-modal="true"
          :aria-label="expandedMedia.title || 'Expanded project media'"
          @click.self="closeMedia"
        >
          <button class="media-modal-close" type="button" aria-label="Close media" @click="closeMedia">
            &times;
          </button>
          <div class="media-modal-content">
            <video
              v-if="expandedMedia.type === 'video'"
              :src="expandedMedia.url"
              controls
              autoplay
              playsinline
            ></video>
            <img
              v-else
              :src="expandedMedia.url"
              :alt="expandedMedia.title || projectInfo.title"
            />
            <p v-if="expandedMedia.title" class="media-modal-title">{{ expandedMedia.title }}</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, inject, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import Header from '@/components/general/Header.vue'

const api = inject("api");
const endpoints = inject('endpoints');

const route = useRoute()
const router = useRouter()

const videoRef = ref(null)
const PREVIEW_VOLUME = 0.30

// Runs once the video's metadata is ready: keep the preview quiet.
const onVideoReady = () => {
  if (videoRef.value) videoRef.value.volume = PREVIEW_VOLUME
}

// The video autoplays muted (browser policy). On the first real interaction
// anywhere on the page, unmute it at a low volume so the demo audio fades in
// instead of jump-scaring the visitor.
const enableSound = () => {
  const video = videoRef.value
  if (video) {
    video.volume = PREVIEW_VOLUME
    video.muted = false
  }
  removeGestureListeners()
}

const gestureEvents = ['pointerdown', 'keydown', 'wheel', 'touchstart']
const removeGestureListeners = () => {
  gestureEvents.forEach((e) => window.removeEventListener(e, enableSound))
}

const projectId = route.params.id
const projectInfo = ref({})
const expandedMedia = ref(null)

const openMedia = (block) => {
  expandedMedia.value = block
  document.body.classList.add('media-modal-open')
}

const closeMedia = () => {
  expandedMedia.value = null
  document.body.classList.remove('media-modal-open')
}

const handleModalKeydown = (event) => {
  if (event.key === 'Escape' && expandedMedia.value) closeMedia()
}

// Detail rows -> render blocks. Media blocks alternate sides: the 1st keeps the
// media on the right, the 2nd flips it to the left, and so on.
const infoBlocks = computed(() => {
  const rows = projectInfo.value?.details ?? []
  let mediaSeen = 0
  return rows.map((row) => {
    const hasMedia = Boolean(row.url)
    const flip = hasMedia && mediaSeen++ % 2 === 1
    return { ...row, hasMedia, flip }
  })
})

onMounted(() =>{
  loadProject();
  window.addEventListener('keydown', handleModalKeydown)
  gestureEvents.forEach((e) =>
    window.addEventListener(e, enableSound, { passive: true })
  )
})

onUnmounted(() => {
  removeGestureListeners()
  window.removeEventListener('keydown', handleModalKeydown)
  document.body.classList.remove('media-modal-open')
})

let loadTimeout = null;
// Watch activeCategory and fetch projects whenever it changes with a delay for exit animation

async function loadProject(){
  try {
    const response = await api.get(`${endpoints.PROJECTS}${projectId}`)
    if (response.status === 200) {
      projectInfo.value = response.data;
      console.log(projectInfo.value);
    }
  } catch (error) {
    console.error(`Error fetching project with id: ${projectId}`, error);
  }
}

const goBack = () => {
  router.push("/")
}
</script>

<style lang="scss" scoped>
@use "sass:color";

.project-detail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  justify-items: center;
  width: 100%;
  gap: 5vh;
}

.project-media{
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

.project-info{
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  width: 100%;
}

.project-short-desc{
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.return-btn {
  display: inline-flex;
  width: 8rem;
  align-items: center;
  gap: 0.5rem;
  font-family: $font-heading;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.6rem 1.4rem;
  border-radius: $border-radius-md;
  border: 1px solid $border-color;
  background: rgba(255, 255, 255, 0.02);
  color: $text-secondary;
  cursor: pointer;
  transition: $transition-normal;
  
  &:hover {
    color: $text-primary;
    border-color: rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.05);
    transform: translateX(-4px);
  }
}

.project-title {
  font-size: 2.5rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #ffffff 30%, #c0c0c0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  
  @include tablet {
    font-size: 2rem;
  }
}

.project-preview-wrapper {
  @include glass-panel($bg-card, $border-color, 16px);
  border-radius: $border-radius-lg;
  overflow: hidden;
  width: 50vw;
  margin-inline: auto;
  box-shadow: $shadow-lg, 0 0 40px rgba($color-dev, 0.15);
  position: relative;
  aspect-ratio: 16 / 9;
  
  video, img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    box-shadow: $shadow-lg 50px 0 40px rgba($color-dev, 0.15);
  }
}

.project-meta {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.01);
  padding: 1.5rem;
  border-radius: $border-radius-md;
  border: 1px solid rgba(255, 255, 255, 0.04);
}

.project-date {
  font-size: 0.95rem;
  font-weight: 600;
  color: $text-muted;
}

.project-status {
  font-size: 0.95rem;
  font-weight: 600;
  color: $color-art;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.project-tech {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.skills_stack,
.techs_stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.tech-badge,
.tech-chip {
  font-size: 0.7rem;
  font-family: $font-mono;
  padding: 0.25rem 0.55rem;
  border-radius: $border-radius-sm;
}

.tech-badge {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  color: $text-secondary;
}

.tech-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba($color-dev, 0.08);
  border: 1px solid rgba($color-dev, 0.22);
  color: $color-dev;
  font-weight: 600;

  &::before {
    content: '';
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: $color-dev;
  }
}

.detail-title {
  border-top: 1px solid $border-color;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.5rem;
  
  h1 {
    font-size: 1.75rem;
    font-weight: 700;
  }
}

.lead {
  font-size: 1.15rem;
  line-height: 1.7;
  color: $text-secondary;
}

.info-layout {
  display: grid;
  grid-template-columns: minmax(9rem, 14rem) minmax(0, 1fr);
  align-items: start;
  gap: 2.5rem;
}

.content-nav {
  position: sticky;
  top: 5rem;
  padding: 1rem;
  border: 1px solid $border-color;
  border-radius: $border-radius-md;
  background: rgba($bg-card, 0.5);
}

.content-nav-title {
  margin-bottom: 0.75rem;
  color: $text-primary;
  font-family: $font-heading;
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.content-nav-list {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  margin: 0;
  padding-left: 1.25rem;

  a {
    color: $text-secondary;
    font-size: 0.9rem;
    line-height: 1.3;
    transition: $transition-fast;

    &:hover {
      color: $color-dev;
    }
  }
}

.info-block {
  scroll-margin-top: 1.5rem;
}

.info-blocks {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
}

.info-block {
  display: flex;
  justify-content: center;
  width: 100%;

  .info-text{
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 50%;

    .h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: $text-primary;
    }

    p {
      font-size: 1.05rem;
      line-height: 1.7;
      color: $text-secondary;
      width: 100%;
    }
  }

  &:not(.has-media) .info-text {
    width: 100%;
  }

  &:not(.has-media) .info-text h3 {
    text-align: center;
  }
  &.has-media {
    display: flex;
    align-items: center;
    gap: 2.5rem;

    .info-text,
    .info-media {
      flex: 1 1 0;
      min-width: 0;
    }

    &.flip {
      flex-direction: row-reverse;
    }

    @include tablet {
      flex-direction: column;
      align-items: stretch;
      gap: 1.5rem;

      &.flip {
        flex-direction: column;
      }
    }
  }
}

.info-media {
  @include glass-panel($bg-card, $border-color, 12px);
  border-radius: $border-radius-lg;
  overflow: hidden;
  aspect-ratio: 16 / 9;
  cursor: zoom-in;
  transition: $transition-normal;

  &:hover,
  &:focus-visible {
    border-color: $border-color-hover;
    box-shadow: $shadow-lg, $glow-dev;
    outline: none;
    transform: translateY(-2px);
  }

  img,
  video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
}

.media-modal {
  position: fixed;
  inset: 0;
  z-index: 20;
  display: grid;
  place-items: center;
  padding: 2rem;
  background: rgba($bg-main, 0.1);
  backdrop-filter: blur(8px);
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.28s ease;

  .media-modal-content {
    transition: transform 0.28s ease;
  }
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;

  .media-modal-content {
    transform: scale(0.96);
  }
}

.media-modal-content {
  position: relative;
  width: min(90vw, 1100px);
  max-height: 90vh;
  overflow: hidden;
  border: 1px solid $border-color-hover;
  border-radius: $border-radius-lg;
  background: $bg-code;
  box-shadow: $shadow-lg, $glow-dev, $glow-art;

  img,
  video {
    display: block;
    width: 100%;
    max-height: 82vh;
    object-fit: contain;
  }
}

.media-modal-close {
  position: fixed;
  top: 1.25rem;
  right: 1.5rem;
  z-index: 1;
  width: 2.5rem;
  height: 2.5rem;
  border: 1px solid $border-color;
  border-radius: 50%;
  background: $bg-card;
  color: $text-primary;
  font-size: 1.5rem;
  line-height: 1;
  cursor: pointer;
  transition: $transition-fast;

  &:hover,
  &:focus-visible {
    border-color: $color-dev;
    box-shadow: $glow-dev;
    color: $color-dev;
    outline: none;
  }
}

.media-modal-title {
  padding: 0.75rem 1rem;
  margin: 0;
  color: $text-secondary;
  font-family: $font-heading;
  text-align: center;
}

.no-details {
  text-align: center;
  color: $text-muted;
  padding: 2rem 0;
}

:global(body.media-modal-open) {
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .modal-fade-enter-active,
  .modal-fade-leave-active,
  .modal-fade-enter-active .media-modal-content,
  .modal-fade-leave-active .media-modal-content {
    transition-duration: 0.01ms;
  }
}

@include tablet {
  .info-layout {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .content-nav {
    position: static;
  }

  .media-modal {
    padding: 1rem;
  }
}
</style>